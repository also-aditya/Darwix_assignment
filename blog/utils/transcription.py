import assemblyai as aai
import os
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transcribe_with_diarization(file_path):
  
    try:
      
        if not os.path.exists(file_path):
            raise Exception(f"Audio file not found: {file_path}")

     
        api_key = os.getenv('ASSEMBLYAI_API_KEY')
        if not api_key:
            raise Exception("ASSEMBLYAI_API_KEY not set in .env")

        aai.settings.api_key = api_key

        
        config = aai.TranscriptionConfig(
            speaker_labels=True,           
            language_detection=True,   
            speakers_expected=2,         
            audio_end_at=60000          
        )

        
        transcriber = aai.Transcriber()
        logger.info(f"Starting transcription for file: {file_path}")

        transcript = transcriber.transcribe(file_path, config=config)

     
        if transcript.status == aai.TranscriptStatus.error:
            raise Exception(f"Transcription failed: {transcript.error}")

      
        if not transcript.utterances:
            logger.warning("No utterances detected in the audio")
            return [{"speaker": "Unknown", "text": transcript.text or "No transcription available", 
                     "start_time": 0.0, "end_time": 0.0}]

        
        result = [
            {
                "speaker": utterance.speaker,
                "text": utterance.text,
                "start_time": utterance.start / 1000.0,
                "end_time": utterance.end / 1000.0
            }
            for utterance in transcript.utterances
        ]

       
        speakers = set(utterance["speaker"] for utterance in result)
        logger.info(f"Detected {len(speakers)} speaker(s): {speakers}")

        return result

    except Exception as e:
        logger.error(f"Transcription error: {str(e)}")
        raise Exception(f"Transcription failed: {str(e)}")
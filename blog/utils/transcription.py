import assemblyai as aai
import os
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transcribe_with_diarization(file_path):
    """
    Transcribe an audio file with speaker diarization using AssemblyAI.
    
    Args:
        file_path (str): Path to the audio file (e.g., .wav, .mp3).
    
    Returns:
        list: List of dictionaries with speaker, text, start_time, and end_time.
    
    Raises:
        Exception: If transcription fails or file is invalid.
    """
    try:
        # Verify file exists and is accessible
        if not os.path.exists(file_path):
            raise Exception(f"Audio file not found: {file_path}")

        # Set AssemblyAI API key
        api_key = os.getenv('ASSEMBLYAI_API_KEY')
        if not api_key:
            raise Exception("ASSEMBLYAI_API_KEY not set in .env")

        aai.settings.api_key = api_key

        # Configure transcription with diarization and auto language detection
        config = aai.TranscriptionConfig(
            speaker_labels=True,           # Enable diarization
            language_detection=True,      # Auto-detect language for better accuracy
            speakers_expected=2,          # Optional: Hint for number of speakers (adjust as needed)
            audio_end_at=60000           # Limit to 60 seconds for testing (adjust for longer files)
        )

        # Initialize transcriber
        transcriber = aai.Transcriber()
        logger.info(f"Starting transcription for file: {file_path}")

        # Transcribe the audio file
        transcript = transcriber.transcribe(file_path, config=config)

        # Check for transcription errors
        if transcript.status == aai.TranscriptStatus.error:
            raise Exception(f"Transcription failed: {transcript.error}")

        # Check if utterances are empty
        if not transcript.utterances:
            logger.warning("No utterances detected in the audio")
            return [{"speaker": "Unknown", "text": transcript.text or "No transcription available", 
                     "start_time": 0.0, "end_time": 0.0}]

        # Format results
        result = [
            {
                "speaker": utterance.speaker,
                "text": utterance.text,
                "start_time": utterance.start / 1000.0,
                "end_time": utterance.end / 1000.0
            }
            for utterance in transcript.utterances
        ]

        # Log number of speakers detected
        speakers = set(utterance["speaker"] for utterance in result)
        logger.info(f"Detected {len(speakers)} speaker(s): {speakers}")

        return result

    except Exception as e:
        logger.error(f"Transcription error: {str(e)}")
        raise Exception(f"Transcription failed: {str(e)}")
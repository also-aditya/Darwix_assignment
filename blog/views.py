from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os
from .utils.transcription import transcribe_with_diarization
from .utils.title_suggestion import generate_titles
import json

@csrf_exempt
def transcribe_audio(request):
    if request.method == 'POST' and 'audio_file' in request.FILES:
        audio_file = request.FILES['audio_file']
        file_path = default_storage.save('temp_audio', audio_file)
        
        try:
            result = transcribe_with_diarization(file_path)
            default_storage.delete(file_path)
            return JsonResponse({"transcription": result}, status=200)
        except Exception as e:
            default_storage.delete(file_path)
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def suggest_titles(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('content', '')
            if not content:
                return JsonResponse({"error": "Content is required"}, status=400)
            titles = generate_titles(content)
            return JsonResponse({"titles": titles}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)
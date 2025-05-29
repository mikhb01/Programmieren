import whisper
import os

def transcribe_audio(audio_file_path, model_name="base", output_dir="transcripts"):
    """
    Transkribiert eine Audiodatei mit OpenAI Whisper.

    Args:
        audio_file_path (str): Der Pfad zur Audiodatei, die transkribiert werden soll.
        model_name (str): Der Name des Whisper-Modells (z.B. "tiny", "base", "small", "medium", "large").
                          "base" ist ein guter Startpunkt.
        output_dir (str): Das Verzeichnis, in dem die Transkriptionsdatei gespeichert werden soll.
    """
    if not os.path.exists(audio_file_path):
        print(f"Fehler: Audiodatei nicht gefunden unter '{audio_file_path}'")
        return

    # Lade das Whisper-Modell
    print(f"Lade Whisper-Modell '{model_name}'... (Dies kann beim ersten Mal etwas dauern)")
    model = whisper.load_model(model_name)
    print("Modell geladen.")

    # Transkribiere die Audiodatei
    print(f"Transkribiere '{audio_file_path}'...")
    result = model.transcribe(audio_file_path)

    # Das Transkript extrahieren
    transcript = result["text"]
    print("\nTranskription abgeschlossen:")
    print(transcript)

    # Speichere das Transkript in einer Textdatei
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    output_file_path = os.path.join(output_dir, f"{base_name}_transcript.txt")

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(transcript)
    print(f"\nTranskript wurde gespeichert in: {output_file_path}")

    # Optional: Speichere auch das detaillierte Ergebnis (z.B. mit Zeitstempeln)
    # import json
    # detailed_output_file_path = os.path.join(output_dir, f"{base_name}_detailed_transcript.json")
    # with open(detailed_output_file_path, "w", encoding="utf-8") as f:
    #     json.dump(result, f, indent=4, ensure_ascii=False)
    # print(f"Detailliertes Transkript wurde gespeichert in: {detailed_output_file_path}")


if __name__ == "__main__":
    # Ersetze 'your_audio_file.mp3' durch den tatsächlichen Pfad zu deiner Audiodatei
    # Beispiel: 'C:/Users/DeinName/Desktop/meeting.wav' oder 'audio/interview.m4a'
    audio_file_to_transcribe = "Part1_speech_23052025_mono-2.wav" # <--- HIER DEINEN DATEIPFAD EINFÜGEN!

    # Du kannst hier das Modell wählen: "tiny", "base", "small", "medium", "large"
    # "base" ist ein guter Startpunkt für Deutsch. Für bessere Genauigkeit "medium" oder "large".
    selected_model = "large"

    transcribe_audio(audio_file_to_transcribe, model_name=selected_model)

    # Um die virtuelle Umgebung zu verlassen, wenn du fertig bist:
    # deactivate
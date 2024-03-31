def run_personality_test():
    print("selamat datang pada tes kepribadian!")
    
    # pertanyaan
    questions = [
        "1. apa anda suka menghabiskan waktu bersama teman dan keluarga? (ya/tidak)",
        "2. apa anda merasa lebih terorganisir daripada spontanitas ? (ya/tidak)",
        "3. apa anda merasa mudah memperkenalkan diri ke orang lain? (ya/tidak)",
        "4. Apa anda merasa tidak suka keramaian? (ya/tidak)",
        "5. Are you often the life of the party? (ya/tidak)"
    ]
    
    # bagian faktor kepribadian
    personality_types = {
        "Introvert": 0,
        "Extrovert": 0
    }
    
    # pertanyaan dan pengambilan jawaban
    for question in questions:
        answer = input(question).strip().lower()
        
        if answer == 'ya':
            personality_types["Introvert"] += 1
        elif answer == 'tidak':
            personality_types["Extrovert"] += 1
        else:
            print("jawaban hanya boleh ya dan tidak")
            return
    
    # rumus menentukan kepribadian
    personality_type = max(personality_types, key=personality_types.get)
    
    print(f"\nKepribadian anda cenderung ke: {personality_type}")
    
    if personality_type == "Introvert":
        print("anda cenderung Introvert. anda suka kedamaian dan melakukan aktivitas sendirian.")
    else:
        print("anda cenderung Extrovert. Anda suka bersosialisasi dan menyukai kegiatan berkelompok.")
    

if __name__ == "__main__":
    run_personality_test()
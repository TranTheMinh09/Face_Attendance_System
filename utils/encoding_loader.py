import os
import pickle

ENCODING_DIR = 'encodings'

def load_all_encodings():
    all_encodings = []
    all_names = []

    if not os.path.exists(ENCODING_DIR):
        print(f"❌ Encoding directory '{ENCODING_DIR}' not found.")
        return [], []

    files = [f for f in os.listdir(ENCODING_DIR) if f.endswith('.pkl')]
    if not files:
        print("⚠️ No encoding files found.")
        return [], []

    print(f"📦 Found {len(files)} encoding file(s):")

    for file in sorted(files):
        path = os.path.join(ENCODING_DIR, file)
        try:
            with open(path, 'rb') as f:
                data = pickle.load(f)

            encs = data.get('encodings')
            name = data.get('name')

            if not encs or not name:
                print(f"⚠️ Skipped invalid file: {file}")
                continue

            all_encodings.extend(encs)
            all_names.extend([name] * len(encs))

            print(f"  ✅ Loaded {len(encs):>3} encoding(s) for: {name}")
        except Exception as e:
            print(f"❌ Failed to load {file}: {e}")

    print(f"\n🧠 Total: {len(all_encodings)} encodings for {len(set(all_names))} person(s).")
    return all_encodings, all_names

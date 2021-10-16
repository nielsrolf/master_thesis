import pandas as pd
from glob import glob
import librosa


dirs = glob("/Users/nielswarncke/Google Drive/ddsp/data/raw/*")

def get_dur(dur):
    hours = int(dur//3600)
    if hours > 0:
        hours = f"{hours}:"
    else:
        hours = "00:"
    dur = dur % 3600
    return f"{hours}{int(dur//60):02d}:{int(dur%60):02d}"

train = 0
test = 0
df = pd.DataFrame(columns=["Dataset", "Audio Data"])
for d in dirs:
    dur = 0
    if "drums" in d:
        continue
    for f in glob(f"{d}/*/*.wav"):
        dur += librosa.get_duration(filename=f)
    print(d, f"{int(dur//60)}:{int(dur%60)}")
    if d == 0:
        continue
    if "train" in d:
       train += dur
    elif "test" in d:
        test += dur
    dur = get_dur(dur)

    df = df.append({"Dataset": d.split("/")[-1], "Audio Data": dur}, ignore_index=True)

print("Combined train", get_dur(train))
print("Combined test", get_dur(test))
df = df.loc[df['Audio Data']!="00:00:00"].sort_values("Dataset")
print(df.to_latex(index=False))
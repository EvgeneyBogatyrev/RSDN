import os
from pathlib import Path

os.system("chmod 0777 /model -R")

with open('/model/run.sh', 'w') as f:
    Path('/model/result').mkdir(parents=True, exist_ok=True)

    _, vids, _ = next(os.walk('/dataset'))

    for vid in vids:
        Path(f"/model/result/{vid}").mkdir(parents=True, exist_ok=True)

        number_of_files = len(os.listdir(f'/dataset/{vid}'))

        with open('/model/list.txt', 'w') as g:
            for i in range(number_of_files):
                g.write(f'frame{str(i + 1).zfill(4)}.png\n')
    
        f.write(f"python3 /model/RSDN/test.py --test_dir /dataset/{vid} --image_out /model/result/{vid} --file_test_list /model/list.txt\n")
    f.write('chmod -R 0777 /model/result\n')

os.system('chmod 0777 /model/run.sh')
os.system('sh /model/run.sh')

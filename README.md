
# SLP Development Manual

## how do run the code?

1. ```  cd {target directory}   ```

2. ```  pip install -r ./requirements.txt   ```

3. ```  python main.py   ```

## what does these code do?

1. main.py: star Scrapering data; if it got errors, the program will stop for 24 hours, and then update package ```snscrape``` with ```  pip install snscrape```

## install CUDA (option)

1. check your GPU version. e.g. NVIDIA GeForce RTX 3060 Ti

2. google 'CUDA Capability GPU': https://developer.nvidia.com/cuda-gpus, and find the compatible version of CUDA e.g. >=8.6

3. download CUDA toolkit: https://developer.nvidia.com/cuda-downloads

4. download pytorch: https://pytorch.org/

## generate requirements.txt (option)

1. ```  python -m  pipreqs.pipreqs --encoding utf-8  ./ --force ```


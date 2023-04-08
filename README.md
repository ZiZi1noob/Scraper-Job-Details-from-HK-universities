
# SLP Development Manual

## how do run the code?

1. ```  cd {target directory}   ```

2. ```  pip install -r ./requirements.txt   ```

3. ```  python main.py   ```

## what does these code do?

1. **main.py**: star Scrapering data; if it got errors, the program will stop for 24 hours, and then update package ```snscrape``` with 

```  
pip install snscrape
```

2. **data**: all data are put under this folder; please donot change any location and name of this folder, or it will cause loading paths failed. If adding folder or chaning names of folder is necessary, please direct to **Config.py** and make corresponsing changes

3. **Config.py**: Again! Go to this file for making any changes on settings paths. And the system will load changes automatically

4. **ModelPrediction.py**: where to apply selected model and make a prediction. ```single_list_pred()``` applies to a list, and ```folder_pred()``` applies to a folder.

5. **Models.py**: stores models' details

6. **NaturalLangProcessing.py**: do prepreocessing stuff...

7. **nice_functions.py**: includes some fundamental, common, and useful functions, like reading file; reading dictionary; calculating ambilence and generating results; writing contents to tsv (most data are stored as .tsv) ...

8. **RAEDFILE.py**: most of operations on folder and files are stored at here; It also has checking-path function (setting ```CHECK_PATH=True``` when calling readFile class)

9. **scraperData.py**: all codes of scrapering data are stored there.
    - sss
    - sdsdads
    - sad s

# **Bonus**

## install CUDA (optional)

1. check your GPU version. e.g. NVIDIA GeForce RTX 3060 Ti

2. google 'CUDA Capability GPU': https://developer.nvidia.com/cuda-gpus, and find the compatible version of CUDA e.g. >=8.6

3. download CUDA toolkit: https://developer.nvidia.com/cuda-downloads

4. download pytorch: https://pytorch.org/

## generate requirements.txt (optional)

1. ``` python -m  pipreqs.pipreqs --encoding utf-8  ./ --force ```

## converting markdown to PDF (optional)

1. 

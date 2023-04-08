
# SLP Development Manual

## install CUDA (option)

1. check your GPU version. e.g. NVIDIA GeForce RTX 3060 Ti

2. google 'CUDA Capability GPU': https://developer.nvidia.com/cuda-gpus and find the compatible version of CUDA e.g. >=8.6

3. download CUDA toolkit: https://developer.nvidia.com/cuda-downloads

4. download pytorch: https://pytorch.org/

## generate requirements.txt

1. ```python -m  pipreqs.pipreqs --encoding utf-8  ./ --force```

To submit your work for autograding on the server, you need to generate a fresh submission token from the Coursera assignment web page. It's a text string you can copy and paste. Then, you need to run the submission script from your workspace directory:

```
python3 ./submit.py
```

It will ask you to enter your Coursera email address and the submission token.

## Local testing

### How do I test if my code passes all the test cases ?

Run the grader. Tests are initiated with `Tester.sh`. You can run this test suite locally like this:

```
$ chmod +x Tester.sh
$ ./Tester.sh
```

### How do I run the CRUD tests separately?

First, compile your project:

```
$ make clean
$ make
```

Then use one of these invocations:

```
$ ./Application ./testcases/create.conf
$ ./Application ./testcases/delete.conf
$ ./Application ./testcases/read.conf
$ ./Application ./testcases/update.conf
```

You may need to do `make clean && make` in between tests to make sure you have a clean run.

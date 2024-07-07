1. Installation:
	pip install dvc

2. Initialize DVC.
	git init
	dvc init ( git init )

3. Download the data from https://www.kaggle.com/datasets/uciml/mushroom-classification
    dvc get <csv file path from downloads> -o data/mushroom.csv
    dvc add data/mushroom.csv
    git add data/mushroom.csv.dvc data/.gitignore

4. Make sure you have mentioned your Github account email ID and Username for github to push data.
    git commit
    mkdir ~/assignments/dvc-storage
    dvc remote add -d tutremote ~/assignments/dvc-storage
    dvc push

5. Delete the files and try to pull from DVC.
	    rm -rf .dvc/cache
        rm -f data/data.xml
        dvc pull

6. Install DVC Extension in Vscode ( Optional )

7. Build Pipelines:
	
	Download the code and extract it.

		wget https://code.dvc.org/get-started/code.zip
		unzip code.zip && rm -f code.zip
	
	Add the following stages to the pipeline.

        Prepare Stage 

        dvc stage add -n prepare -d src/prepare.py -d data/mushrooms.csv \
                    -p prepare.seed -p prepare.split -o data/prepared \
                    python src/prepare.py data/mushrooms.csv

        Featurise Stage

		dvc stage add -n featurise -d src/featurization.py -d data/prepared \
                    -o data/encoded python src/featurization.py data/prepared data/encoded

        Train Stage

		dvc stage add -n train -p train.seed -p train.n_est -p train.min_split \
                    -d src/train.py -d data/encoded -o model.pkl \
                    python src/train.py data/encoded model.pkl

        Adding other files to commit

		git add .gitignore data/.gitignore dvc.yaml
		git commit -m "pipeline defined"   
	
	Visualize the pipeline

		dvc dag
	
	Run/Reproduce the pipeline

		dvc repro
		
	Add and track experiments.

        dvc stage add -n evaluate -d src/evaluate.py \
                    -d model.pkl -d data/encoded -o eval \
                    python src/evaluate.py model.pkl data/encoded

	Run/Reproduce the pipeline

		dvc repro

	git add .gitignore dvc.yaml dvc.lock eval
    git commit -a -m "Create evaluation stage"

    dvc metrics show
	
	Review the metrics on the DVC extensions (Optional).
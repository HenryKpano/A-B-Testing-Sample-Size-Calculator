Calsulating the required sample size for A/B TESTING

Using a virtual Env

Open new terminal

Create new directory: mkdir sample

Open directory: cd sample

Create virtualenv: python3 -m venv venv

Activate env: source venv/bin/activate

Upgrade pip: pip install --upgrade pip

Intall statistical model: This would install all the packages that are needed
: pip install statsmodels

Run py file: python sample_size.py


Example (Sample_size.py)

The sample uses some assumptions
- Conversion rate expected is 50% which is serves as the initial conversion rate
- power of 80%
- alpha of 5%


Alternatively 
-Use the Jupyter Notebook version in this repo as well

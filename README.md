# PCA_web_method

This is a Flask based web REST service to use Singular Value Decomposition to provide dimensionality reduction via PCA.<br>
This code implements PCA web service build on top of scikit-learn decompositions method PCA and IncrementalPCA.<br>

## INSTRUCTIONS TO TEST LOCALLY
1. cd "your working directory"<br>
1. create a virtual environment via: `virtualenv "your_virtual_env_name"`<br>
1. activate virtual env: (linux) `source "your_virtual_env_name"/bin/activate` (windows) `.\"your_virtual_env_name"\Script\activate.bat`<br> 
1. clone repository<br>
1. run: `pip install -r requirements.txt`<br>

once all dependecies installed...

__testing:__
this command will run all unit tests

`python manage.py test`

__launch in localhost:__
this comand will launch the flask resfull API, remember set enviromental variables (see next section)

`python manage.py run`

### DEPLOY ON DOCKER
1. clone this repository
2. open a shell
3. cd to the directory where the repository has been downloaded
4. build the image:  `docker build -t <<image_name>> .`
5. run the image with the desired environmental variables (see next section): Ex.`docker run --env=”API_PORT=8000” --env"API_PROTOCOL=http" -p 8000:8000 <<image_name>>:latest`

## ENVIRONMENT VARIABLES
 - *API_PROTOCOL*: 
    - values: http,https(default)
    - desc:workaround to display swagger documentation in http or https<br>
 - *WORKING_ENV*:  
    - values:test,dev,prod
    - desc:sets the working environment to test, development or production<br>
 - *API_HOST*: 
    - values: any,0.0.0.0(default)
    - desc: the domain where the API is hosted, by default the host machine<br>
 - *API_PORT*: 
    - values: any available port, 5000(default)
    - desc: the port to expose the API
 - *LOG_LEVEL*: 
    - values:debug,info,warning,error,critical
    - desc: threshold logging level to manage which messages will be showed<br>


## USAGE
The API exposes two methods explained below

For further info swagger documentation can be found under https://localhost:5000/docs/ (when using the default environment variables and running locally, update URL accordingly). 

### pca/train
POST method
calculates the pca, given the methodology:
- options:
    - pca: classic pca method applying a previous standard scaler to data provided.
    - pca_raw: classic pca method without applying a previous standard scaler.
    - ipca: incremental pca method applying a previous standard scaler to use with large datasets.(batch_size must be specified)
    - ipca_raw: incremental pca method without applying a previous standard scaler.(batch _size must be specified)
- query: please check app/main/model/connect_db.py to complete the datat link
- raw_data: json serialized input stream format:{"columns":[],"index":[],"data":[[]]}
- n_components: number of components desired

*Example of test train call:*
note that query:"test" just loads the infamous [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) to emulate the query
```
{
  "dataDesc": {
    "query": "test" 
  },
  "options": "pca",
  "n_components":3
}
```
will return:
```
{
  "status": "ok",
  "components": [
    [
      0.5210659146701195,
      -0.26934744250594367,
      0.5804130957962945,
      0.5648565357793612
    ],
    [
      0.3774176155645673,
      0.9232956595407151,
      0.024491609085586785,
      0.06694198696805842
    ],
    [
      -0.7195663527008169,
      0.2443817795143992,
      0.1421263693339043,
      0.6342727371109227
    ]
  ],
  "explained_variance": [
    2.9380850501999953,
    0.9201649041624886,
    0.14774182104494812
  ],
  "explained_variance_ratio": [
    0.7296244541329985,
    0.2285076178670179,
    0.036689218892828765
  ],
  "singular values": [
    20.923065561236463,
    11.709166098412423,
    4.6918579833257175
  ],
  "n_components": 3,
  "noise_variance": 0.020853862176462328,
  "model_stream": "gANC5wUAAIADY3NrbGVhcm4ucGlwZWxpbmUKUGlwZWxpbmUKcQApgXEBfXECKFgFAAAAc3RlcHNx\nA11xBChYBgAAAHNjYWxlcnEFY3NrbGVhcm4ucHJlcHJvY2Vzc2luZy5kYXRhClN0YW5kYXJkU2Nh\nbGVyCnEGKYFxB31xCChYCQAAAHdpdGhfbWVhbnEJiFgIAAAAd2l0aF9zdGRxCohYBAAAAGNvcHlx\nC4hYDwAAAG5fc2FtcGxlc19zZWVuX3EMY251bXB5LmNvcmUubXVsdGlhcnJheQpzY2FsYXIKcQ1j\nbnVtcHkKZHR5cGUKcQ5YAgAAAGk4cQ9LAEsBh3EQUnERKEsDWAEAAAA8cRJOTk5K/////0r/////\nSwB0cRNiQwiWAAAAAAAAAHEUhnEVUnEWWAUAAABtZWFuX3EXY251bXB5LmNvcmUubXVsdGlhcnJh\neQpfcmVjb25zdHJ1Y3QKcRhjbnVtcHkKbmRhcnJheQpxGUsAhXEaQwFicRuHcRxScR0oSwFLBIVx\nHmgOWAIAAABmOHEfSwBLAYdxIFJxIShLA2gSTk5OSv////9K/////0sAdHEiYolDIGEs+cWSXxdA\nRBm9LWt1CECw8dJNYhAOQJq1OiZ4MPM/cSN0cSRiWAQAAAB2YXJfcSVoGGgZSwCFcSZoG4dxJ1Jx\nKChLAUsEhXEpaCGJQyDIvqDUwMvlP0hEDnO+J8g/7hzw5pbDCEAzKWdk33fiP3EqdHErYlgGAAAA\nc2NhbGVfcSxoGGgZSwCFcS1oG4dxLlJxLyhLAUsEhXEwaCGJQyAbCjJB3mjqP3Sm3Khjzds/D0Wv\n4IQm/D8sRPvpZk/oP3ExdHEyYlgQAAAAX3NrbGVhcm5fdmVyc2lvbnEzWAYAAAAwLjIwLjNxNHVi\nhnE1WAMAAABwY2FxNmNza2xlYXJuLmRlY29tcG9zaXRpb24ucGNhClBDQQpxNymBcTh9cTkoWAwA\nAABuX2NvbXBvbmVudHNxOksDaAuIWAYAAAB3aGl0ZW5xO4lYCgAAAHN2ZF9zb2x2ZXJxPFgEAAAA\nYXV0b3E9WAMAAAB0b2xxPkcAAAAAAAAAAFgOAAAAaXRlcmF0ZWRfcG93ZXJxP2g9WAwAAAByYW5k\nb21fc3RhdGVxQE5YDwAAAF9maXRfc3ZkX3NvbHZlcnFBWAQAAABmdWxscUJoF2gYaBlLAIVxQ2gb\nh3FEUnFFKEsBSwSFcUZoIYlDIDMzMzMzc968mpmZmZmZ4LyamZmZmZnevGPJL5b8Ytm8cUd0cUhi\nWA8AAABub2lzZV92YXJpYW5jZV9xSWgNaCFDCNs7LAC3WpU/cUqGcUtScUxYCgAAAG5fc2FtcGxl\nc19xTUuWWAsAAABuX2ZlYXR1cmVzX3FOSwRYCwAAAGNvbXBvbmVudHNfcU9oGGgZSwCFcVBoG4dx\nUVJxUihLAUsDSwSGcVNoIYlDYBIx0mySrOA/0MA0Dv080b+4rxN8vpLiP7FVgwNOE+I/+i7yNpwn\n2D8ShMhWo4vtPyAwMhBUFJk/SM/BLBwjsT9E3QQEsAbnvxhWYPPmR88/ZxsYZjIxwj+gWNRW9kvk\nP3FUdHFVYlgNAAAAbl9jb21wb25lbnRzX3FWSwNYEwAAAGV4cGxhaW5lZF92YXJpYW5jZV9xV2gY\naBlLAIVxWGgbh3FZUnFaKEsBSwOFcVtoIYlDGNLNG7wygQdAcMFJq/1x7T9X3NE4NOnCP3FcdHFd\nYlgZAAAAZXhwbGFpbmVkX3ZhcmlhbmNlX3JhdGlvX3FeaBhoGUsAhXFfaBuHcWBScWEoSwFLA4Vx\nYmghiUMYW54bYhVZ5z8sF9DUvD/NP0ZehebtyKI/cWN0cWRiWBAAAABzaW5ndWxhcl92YWx1ZXNf\ncWVoGGgZSwCFcWZoG4dxZ1JxaChLAUsDhXFpaCGJQxgSk00GTuw0QP85oNEXaydAH3FPa3bEEkBx\nanRxa2JoM2g0dWKGcWxlWAYAAABtZW1vcnlxbU5oM2g0dWIucQAu\n"
}
```

Please refer to [scikit learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) for a deeper understanding of each returned element.
Additionaly, "model_stream" returns the serialised model to be used in calls to the pca/eval method. 

### pca/eval
evals the pca 
- "dataDesc": follows the input from previous method
- "n_components": sets the number of components to be returned (it can be equal or less to the components provided by the pca model
- "raw_model": model serialised returned by "model _stream"

*Example of test eval call:*
```
{
  "dataDesc": {
    "query": "test"
  },
  "n_components": 2,
  "raw_model": "gANC5wUAAIADY3NrbGVhcm4ucGlwZWxpbmUKUGlwZWxpbmUKcQApgXEBfXECKFgFAAAAc3RlcHNx\nA11xBChYBgAAAHNjYWxlcnEFY3NrbGVhcm4ucHJlcHJvY2Vzc2luZy5kYXRhClN0YW5kYXJkU2Nh\nbGVyCnEGKYFxB31xCChYCQAAAHdpdGhfbWVhbnEJiFgIAAAAd2l0aF9zdGRxCohYBAAAAGNvcHlx\nC4hYDwAAAG5fc2FtcGxlc19zZWVuX3EMY251bXB5LmNvcmUubXVsdGlhcnJheQpzY2FsYXIKcQ1j\nbnVtcHkKZHR5cGUKcQ5YAgAAAGk4cQ9LAEsBh3EQUnERKEsDWAEAAAA8cRJOTk5K/////0r/////\nSwB0cRNiQwiWAAAAAAAAAHEUhnEVUnEWWAUAAABtZWFuX3EXY251bXB5LmNvcmUubXVsdGlhcnJh\neQpfcmVjb25zdHJ1Y3QKcRhjbnVtcHkKbmRhcnJheQpxGUsAhXEaQwFicRuHcRxScR0oSwFLBIVx\nHmgOWAIAAABmOHEfSwBLAYdxIFJxIShLA2gSTk5OSv////9K/////0sAdHEiYolDIGEs+cWSXxdA\nRBm9LWt1CECw8dJNYhAOQJq1OiZ4MPM/cSN0cSRiWAQAAAB2YXJfcSVoGGgZSwCFcSZoG4dxJ1Jx\nKChLAUsEhXEpaCGJQyDIvqDUwMvlP0hEDnO+J8g/7hzw5pbDCEAzKWdk33fiP3EqdHErYlgGAAAA\nc2NhbGVfcSxoGGgZSwCFcS1oG4dxLlJxLyhLAUsEhXEwaCGJQyAbCjJB3mjqP3Sm3Khjzds/D0Wv\n4IQm/D8sRPvpZk/oP3ExdHEyYlgQAAAAX3NrbGVhcm5fdmVyc2lvbnEzWAYAAAAwLjIwLjNxNHVi\nhnE1WAMAAABwY2FxNmNza2xlYXJuLmRlY29tcG9zaXRpb24ucGNhClBDQQpxNymBcTh9cTkoWAwA\nAABuX2NvbXBvbmVudHNxOksDaAuIWAYAAAB3aGl0ZW5xO4lYCgAAAHN2ZF9zb2x2ZXJxPFgEAAAA\nYXV0b3E9WAMAAAB0b2xxPkcAAAAAAAAAAFgOAAAAaXRlcmF0ZWRfcG93ZXJxP2g9WAwAAAByYW5k\nb21fc3RhdGVxQE5YDwAAAF9maXRfc3ZkX3NvbHZlcnFBWAQAAABmdWxscUJoF2gYaBlLAIVxQ2gb\nh3FEUnFFKEsBSwSFcUZoIYlDIDMzMzMzc968mpmZmZmZ4LyamZmZmZnevGPJL5b8Ytm8cUd0cUhi\nWA8AAABub2lzZV92YXJpYW5jZV9xSWgNaCFDCNs7LAC3WpU/cUqGcUtScUxYCgAAAG5fc2FtcGxl\nc19xTUuWWAsAAABuX2ZlYXR1cmVzX3FOSwRYCwAAAGNvbXBvbmVudHNfcU9oGGgZSwCFcVBoG4dx\nUVJxUihLAUsDSwSGcVNoIYlDYBIx0mySrOA/0MA0Dv080b+4rxN8vpLiP7FVgwNOE+I/+i7yNpwn\n2D8ShMhWo4vtPyAwMhBUFJk/SM/BLBwjsT9E3QQEsAbnvxhWYPPmR88/ZxsYZjIxwj+gWNRW9kvk\nP3FUdHFVYlgNAAAAbl9jb21wb25lbnRzX3FWSwNYEwAAAGV4cGxhaW5lZF92YXJpYW5jZV9xV2gY\naBlLAIVxWGgbh3FZUnFaKEsBSwOFcVtoIYlDGNLNG7wygQdAcMFJq/1x7T9X3NE4NOnCP3FcdHFd\nYlgZAAAAZXhwbGFpbmVkX3ZhcmlhbmNlX3JhdGlvX3FeaBhoGUsAhXFfaBuHcWBScWEoSwFLA4Vx\nYmghiUMYW54bYhVZ5z8sF9DUvD/NP0ZehebtyKI/cWN0cWRiWBAAAABzaW5ndWxhcl92YWx1ZXNf\ncWVoGGgZSwCFcWZoG4dxZ1JxaChLAUsDhXFpaCGJQxgSk00GTuw0QP85oNEXaydAH3FPa3bEEkBx\nanRxa2JoM2g0dWKGcWxlWAYAAABtZW1vcnlxbU5oM2g0dWIucQAu\n"
}
```
will return:
```
{
  "status": "ok",
  "transformed_data": [
    [
      -2.2647028088075882,
      0.4800265965209891
    ],
    [
      -2.0809611519657665,
      -0.6741335566053532
    ],
    [
      -2.3642290538903,
      -0.34190802388467645
    ],
    [
      -2.299384217042707,
      -0.5973945076746758
    ],
    [
      -2.3898421663138447,
      0.6468353829020269
    ],
    [
      -2.0756309481765127,
      1.4891775233211668
    ],
    [
      -2.444028835134152,
      0.04764419763001411
    ],
    [
      -2.2328471588720147,
      0.2231480726895916
    ],
    [
      -2.33464047790762,
      -1.1153276754616668
    ],
    [
      -2.184328174933941,
      -0.4690135614023761
    ],
    [
      -2.1663101007013226,
      1.0436906530538597
    ],
    [
      -2.326130866442698,
      0.13307833523923154
    ],
    [
      -2.2184508988224083,
      -0.7286761653165712
    ],
    [
      -2.6331006957652265,
      -0.9615067291701633
    ],
    [
      -2.1987406032666907,
      1.860057113293931
    ],
    [
      -2.2622145316010225,
      2.686284485110592
    ],
    [
      -2.207587695824593,
      1.4836093631555725
    ],
    [
      -2.1903495091922984,
      0.4888383164863275
    ],
    [
      -1.8985719958028424,
      1.405018794466549
    ],
    [
      -2.3433690530749933,
      1.127849381908476
    ],
    [
      -1.9143229960825674,
      0.40885570775590596
    ],
    [
      -2.207012843194798,
      0.9241214267468985
    ],
    [
      -2.7743447029273316,
      0.45834366775291524
    ],
    [
      -1.8186695286958485,
      0.08555852628736592
    ],
    [
      -2.2271633057066382,
      0.13725445536342729
    ],
    [
      -1.9518463309003748,
      -0.6256185877766769
    ],
    [
      -2.051151372729415,
      0.24216355266166695
    ],
    [
      -2.168577174654216,
      0.5271495253082672
    ],
    [
      -2.1395634513013313,
      0.31321781013995165
    ],
    [
      -2.26526149315424,
      -0.3377319037604808
    ],
    [
      -2.1401221356479834,
      -0.5045406901415186
    ],
    [
      -1.831594770676028,
      0.42369506760378556
    ],
    [
      -2.614947935858935,
      1.7935758561044284
    ],
    [
      -2.4461773916965157,
      2.1507278773929244
    ],
    [
      -2.1099748753186516,
      -0.4602018414370377
    ],
    [
      -2.2078088990782647,
      -0.20610739768843725
    ],
    [
      -2.0451462067542012,
      0.6615581114631078
    ],
    [
      -2.527331913170486,
      0.5922927741908093
    ],
    [
      -2.429632575084545,
      -0.9041800403761482
    ],
    [
      -2.169710711630663,
      0.26887896143547063
    ],
    [
      -2.28647514334567,
      0.44171538769904983
    ],
    [
      -1.858122456373569,
      -2.3374151575533486
    ],
    [
      -2.553638395614355,
      -0.47910069012231415
    ],
    [
      -1.9644476837637401,
      0.47232666771926074
    ],
    [
      -2.137059005811623,
      1.142229262039409
    ],
    [
      -2.0697442995918287,
      -0.7110527253858944
    ],
    [
      -2.384733165778263,
      1.1204297019845364
    ],
    [
      -2.394376314219632,
      -0.38624687258915735
    ],
    [
      -2.2294465479426746,
      0.9979597643079802
    ],
    [
      -2.2038334355191296,
      0.009216357521275975
    ],
    [
      1.1017811830529474,
      0.8629724182621591
    ],
    [
      0.7313374253960873,
      0.5946147256694247
    ],
    [
      1.240979319515831,
      0.6162976544374985
    ],
    [
      0.40748305881738667,
      -1.7544039893234107
    ],
    [
      1.0754747006090786,
      -0.20842104605096543
    ],
    [
      0.3886873365356657,
      -0.5932836359900749
    ],
    [
      0.7465297413291605,
      0.773019312098597
    ],
    [
      -0.487322742125638,
      -1.8524290868575746
    ],
    [
      0.9279016383549455,
      0.032226077891153865
    ],
    [
      0.011426188736981258,
      -1.0340182751294404
    ],
    [
      -0.11019628000062677,
      -2.6540728185365645
    ],
    [
      0.4406934489830787,
      -0.06329518843800133
    ],
    [
      0.5621083064431803,
      -1.7647243806169457
    ],
    [
      0.7195618886754969,
      -0.1862246058315056
    ],
    [
      -0.03335470317877165,
      -0.43900320998162473
    ],
    [
      0.8754071908577375,
      0.5090639567734087
    ],
    [
      0.3502516679950831,
      -0.19631173455144377
    ],
    [
      0.1588100475479721,
      -0.7920957424327214
    ],
    [
      1.225093633562433,
      -1.622243803091502
    ],
    [
      0.16491789938632845,
      -1.3026092302957728
    ],
    [
      0.7376826487712582,
      0.3965715619602393
    ],
    [
      0.47628719094097194,
      -0.4173202812135509
    ],
    [
      1.23417809765715,
      -0.9333257287992783
    ],
    [
      0.6328581997098223,
      -0.41638772088909926
    ],
    [
      0.7026611831361825,
      -0.06341181972480013
    ],
    [
      0.8742736538812904,
      0.2507933929006121
    ],
    [
      1.2565091165418838,
      -0.07725601969586886
    ],
    [
      1.358405121440632,
      0.33131168179089826
    ],
    [
      0.6648003672253952,
      -0.22592785469484344
    ],
    [
      -0.04025861090059442,
      -1.058718546553909
    ],
    [
      0.1307951754978619,
      -1.5622718342099677
    ],
    [
      0.02345268897055211,
      -1.5724755942167048
    ],
    [
      0.24153827295451172,
      -0.7772563825848418
    ],
    [
      1.0610946088426148,
      -0.6338432447349466
    ],
    [
      0.22397877351238024,
      -0.287773512043202
    ],
    [
      0.4291391155161604,
      0.845582240905079
    ],
    [
      1.0487280512090873,
      0.5220517968629428
    ],
    [
      1.0445313843962805,
      -1.3829887191907821
    ],
    [
      0.06958832111642335,
      -0.21950333464771485
    ],
    [
      0.28347723828757654,
      -1.3293246390695765
    ],
    [
      0.27907777605546197,
      -1.120028523742404
    ],
    [
      0.6245697914985717,
      0.024923029254012817
    ],
    [
      0.3365303701314368,
      -0.9884040176703602
    ],
    [
      -0.36218338461938143,
      -2.019237873238612
    ],
    [
      0.28858623882315826,
      -0.8557303199870663
    ],
    [
      0.0913606556545058,
      -0.18119212582577512
    ],
    [
      0.22771686553470064,
      -0.3849200809873538
    ],
    [
      0.576388288653479,
      -0.1548735972165588
    ],
    [
      -0.4476670190286103,
      -1.5437920343977565
    ],
    [
      0.2567305888875854,
      -0.5988517961556692
    ],
    [
      1.8445688677230287,
      0.870421312324824
    ],
    [
      1.1578816132057805,
      -0.6988698623306902
    ],
    [
      2.205266791075378,
      0.5620104770083559
    ],
    [
      1.4401506638275396,
      -0.046987588105806236
    ],
    [
      1.8678122203305378,
      0.2950448244570201
    ],
    [
      2.751873335666277,
      0.8004092010275424
    ],
    [
      0.36701768786072597,
      -1.5615028914765055
    ],
    [
      2.3024394446251972,
      0.4200655796427767
    ],
    [
      2.0066864676766065,
      -0.7114386535471586
    ],
    [
      2.2597773490124995,
      1.9210103764598871
    ],
    [
      1.3641754921860076,
      0.6927564544903875
    ],
    [
      1.6026786704779312,
      -0.421700449772617
    ],
    [
      1.8839007017032428,
      0.4192496506051238
    ],
    [
      1.2601150991975087,
      -1.1622604214064634
    ],
    [
      1.4676452010173247,
      -0.4422715873770821
    ],
    [
      1.5900773176145657,
      0.6762448057233205
    ],
    [
      1.4714314611333181,
      0.25562182447147086
    ],
    [
      2.4263289873156992,
      2.556661250795493
    ],
    [
      3.310695583933888,
      0.017780949320627196
    ],
    [
      1.2637666736398294,
      -1.7067453803762678
    ],
    [
      2.0377163014694046,
      0.9104674096183113
    ],
    [
      0.9779807342494222,
      -0.5717643248129916
    ],
    [
      2.897651490734169,
      0.41364105959564806
    ],
    [
      1.3332321759732095,
      -0.4818112186494292
    ],
    [
      1.700733897491217,
      1.0139218673227919
    ],
    [
      1.9543267058530707,
      1.007777596153453
    ],
    [
      1.1751036315549332,
      -0.3163944723097909
    ],
    [
      1.0209505506957912,
      0.0643460292395621
    ],
    [
      1.788349920179666,
      -0.18736121459082844
    ],
    [
      1.863647553328261,
      0.5622907258861449
    ],
    [
      2.435953727922704,
      0.2592844331442805
    ],
    [
      2.304927721831763,
      2.6263234682323793
    ],
    [
      1.862703219794956,
      -0.17854949462549008
    ],
    [
      1.114147740686475,
      -0.29292262333573116
    ],
    [
      1.2024733016783917,
      -0.8113152708396685
    ],
    [
      2.7987704475781077,
      0.8568033294971056
    ],
    [
      1.576255910194754,
      1.0685811073208082
    ],
    [
      1.3462921036270619,
      0.4224306108525087
    ],
    [
      0.9248249165424196,
      0.017223100452284403
    ],
    [
      1.85204505176767,
      0.6761281744365217
    ],
    [
      2.014810429954876,
      0.6138856369235755
    ],
    [
      1.901784090262189,
      0.6895754942430028
    ],
    [
      1.1578816132057805,
      -0.6988698623306902
    ],
    [
      2.0405582280520926,
      0.8675206009552289
    ],
    [
      1.9981470959523762,
      1.0491687471841455
    ],
    [
      1.870503292956411,
      0.3869660816657257
    ],
    [
      1.564580483030329,
      -0.8966868088965262
    ],
    [
      1.521170499627838,
      0.26906914427795187
    ],
    [
      1.3727877895140725,
      1.0112544185267935
    ],
    [
      0.9606560300371282,
      -0.02433166816939898
    ]
  ]
}
```
### Credits
Alejandro Medrano - amedrano@lst.tfo.upm.es
Javier Rojo - jlacal@lst.tfo.upm.es
This work stands on the shoulders of some great libraries, check requirements.txt for more information.

### License
Apache-2.0

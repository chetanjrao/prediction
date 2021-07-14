from analyze.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from prediction.settings import CLASSIFICATION_MODEL
from django.shortcuts import redirect, render
from django.core.handlers.wsgi import WSGIRequest
import numpy as np
import pandas as pd

# Create your views here.
def index(request: WSGIRequest):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create(first_name=name, mobile=mobile, email=email, age=age, gender=gender)
        login(request, user)
        return redirect('predict')
    return render(request, "index.html")

def signout(request: WSGIRequest):
    logout(request)
    return redirect('index')

@login_required(login_url='/')
def predict(request: WSGIRequest):
    if request.method == "POST":
        input_features = [float(x) for x in list(request.POST.values())[1:]]

        # Converting the input features from list to numpy array
        features_value = [np.array(input_features)]

        # Mapping the feature labels to feature values
        features_name=['radius_mean', 'texture_mean', 'perimeter_mean',
        'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
        'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
        'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
        'fractal_dimension_se', 'radius_worst', 'texture_worst',
        'perimeter_worst', 'area_worst', 'smoothness_worst',
        'compactness_worst', 'concavity_worst', 'concave points_worst',
        'symmetry_worst', 'fractal_dimension_worst']

        # Convert the labels and data array to a DataFrame
        df = pd.DataFrame(features_value, columns=features_name)

        ''' 
            Predict the binary classification output from the model
            If output is equal to 1, then the person has breast cancer
            If output is equal to 0,  then the person does not have breast cancer
        '''
        output = CLASSIFICATION_MODEL.predict(df)
        res_val = "has breast cancer" if output == 1 else "does not have breast cancer"
        return render(request, "predict.html", { "prediction_text": 'Patient {} {}'.format(request.user.first_name, res_val) })
    return render(request, "predict.html")
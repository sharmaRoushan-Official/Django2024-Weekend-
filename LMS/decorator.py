from django.shortcuts import render

def is_CheckinloginorRegister(func): # Decorator to check if user is logged in
    def inner(request): # Inner function to wrap the original function
        if request.user.is_authenticated: # Check if the user is logged in
            return render(request,"LMS/dashboard.html") # If logged in, call the original function
        else: # If not logged in
            return func(request) # If not logged in, still call the original function
    return inner # Return the inner function
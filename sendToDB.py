from firebase import firebase
 

def send(path, param, value):

	request = firebase.FirebaseApplication('https://rrsecuritysystem-16709.firebaseio.com/', None)

	result = request.patch("/users/Bk7d978WLsUie3VScUmqpWL9kz03"+path, { param : value }) 

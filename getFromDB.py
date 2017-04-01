from firebase import firebase

firebase = firebase.FirebaseApplication('https://rrsecuritysystem-16709.firebaseio.com/', None)


def query (path):

        estado = firebase.get("users/Bk7d978WLsUie3VScUmqpWL9kz03"+path, None)

        return estado

# Emodon
API Documentation
La documentation des endpoints disponibles pour FacturaSieli est décrite ci-dessous. Ces endpoints permettent de gérer les forums et les choix de mood.

Base URL
Tous les endpoints sont accessibles depuis la base URL suivante :


http://<domaine_ou_ip>/api/

Endpoints

1. Récupérer les choix de mood
URL : /mood_choices/
Méthode : GET
Description : Renvoie la liste des choix de mood disponibles.
Exemple de réponse :

json
{
    "data": [
        {"key": "Happy", "value": 1},
        {"key": "Sad", "value": 2},
        {"key": "Excited", "value": 3}
    ]
}
2. Lister tous les forums
URL : /forums/
Méthode : GET
Description : Récupère tous les forums existants, triés par date de création (plus récent en premier).

Exemple de réponse :
json
{
    "data": [
        {
            "id": 1,
            "title": "Happy",
            "created_at": "2024-12-08T12:00:00Z"
        },
        {
            "id": 2,
            "title": "Sad",
            "created_at": "2024-12-07T15:45:00Z"
        }
    ]
}

3. Créer un forum

URL : /forums/
Méthode : POST
Description : Crée un nouvel objet Forum en fonction du choix de mood fourni.

Requête attendue :
json
{
    "mood_choice": "Happy"
}

Exemple de réponse (succès) :

json
{
    "data": {
        "id": 3,
        "title": "Happy",
        "created_at": "2024-12-08T13:00:00Z"
    },
    "message": "Your forum has been successfully created."
}

Exemple de réponse (échec) :
json
{
    "message": "Mood choice is required."
}

4. Récupérer un forum spécifique

URL : /forums/<forum_id>/
Méthode : GET
Description : Récupère un objet Forum spécifique en fonction de son ID.

Exemple de réponse (succès) :
json
{
    "data": {
        "id": 1,
        "title": "Happy",
        "created_at": "2024-12-08T12:00:00Z"
    },
    "message": "Forum has been found."
}

Exemple de réponse (échec) :
json
{
    "message": "No forum was found."
}

5. Supprimer un forum

URL : /forums/<forum_id>/
Méthode : DELETE
Description : Supprime un objet Forum spécifique.
Exemple de réponse (succès) :

json
{
    "message": "Forum has been successfully deleted."
}
Exemple de réponse (échec) :

json
{
    "message": "No forum was found."
}


Notes importantes
Codes de statut HTTP :

200 OK : Requête réussie.
201 Created : Objet créé avec succès.
400 Bad Request : Erreur dans la requête (données manquantes ou invalides).
404 Not Found : Objet non trouvé.


Données obligatoires pour le front-end :

Vérifiez toujours la validité des réponses et gérez les erreurs (message) affichées dans les exemples ci-dessus.
Exemple d’intégration dans React :

Vous pouvez utiliser fetch ou une bibliothèque comme Axios pour appeler ces endpoints depuis votre application React.

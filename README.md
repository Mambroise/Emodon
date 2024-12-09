# Emodon
# Emodon API Documentation

La documentation ci-dessous décrit les endpoints disponibles pour l’API de **FacturaSieli**. Ces endpoints permettent de gérer les choix de mood, les forums, les réactions, et les emojis.

## Base URL

Tous les endpoints sont accessibles depuis la base URL suivante :

```
https://emodon.onrender.com/api/
```

---

## Endpoints

### 1. Récupérer les choix de mood

**URL :** `/mood_choices/`  
**Méthode :** `GET`  
**Description :** Renvoie la liste des choix de mood disponibles.  

**Exemple de réponse :**
```json
{
    "data": [
        {"key":'bad',"value":'I feel bad'},
        {"key":'alone',"value":'I feel lonely'},
        {"key":'depressed',"value":'I feel depressed'},
        {"key":'hard',"value":'Life is so hard'},
        {"key":'useless',"value":'I feel useless'},

}
```

---

### 2. Récupérer les choix d'emojis

**URL :** `/emoji_choices/`  
**Méthode :** `GET`  
**Description :** Renvoie la liste des emojis disponibles.  

**Exemple de réponse :**
```json
{
    "data": [
        {"key": "kiss", "value": 😘},
        {"key": "heart", "value": ❤️},
        {"key": "smile", "value": 😊},}
    ]
}
```

---

### 3. Lister tous les forums

**URL :** `/forums/`  
**Méthode :** `GET`  
**Description :** Récupère tous les forums existants, triés par date de création (plus récent en premier).

**Exemple de réponse :**
```json
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
```

---

### 4. Créer un forum

**URL :** `/forums/`  
**Méthode :** `POST`  
**Description :** Crée un nouvel objet Forum en fonction du choix de mood fourni.

**Requête attendue :**
```json
{
    "mood_choice": "sad"
}
```

**Exemple de réponse (succès) :**
```json
{
    "data": {
        "id": 3,
        "title": "sad",
        "created_at": "2024-12-08T13:00:00Z"
    },
    "message": "Your forum has been successfully created."
}
```

**Exemple de réponse (échec) :**
```json
{
    "message": "Mood choice is required."
}
```

---

### 5. Récupérer un forum spécifique

**URL :** `/forums/<forum_id>/`  
**Méthode :** `GET`  
**Description :** Récupère un objet Forum spécifique en fonction de son ID.

**Exemple de réponse (succès) :**
```json
{
    "data": {
        "id": 1,
        "title": "sad",
        "created_at": "2024-12-08T12:00:00Z"
    },
    "message": "Forum has been found."
}
```

**Exemple de réponse (échec) :**
```json
{
    "message": "No forum was found."
}
```

---

### 6. Supprimer un forum

**URL :** `/forums/<forum_id>/`  
**Méthode :** `DELETE`  
**Description :** Supprime un objet Forum spécifique.

**Exemple de réponse (succès) :**
```json
{
    "message": "Forum has been successfully deleted."
}
```

**Exemple de réponse (échec) :**
```json
{
    "message": "No forum was found."
}
```

---

### 7. Lister toutes les réactions d'un forum

**URL :** `/reactions/<forum_id>`  
**Méthode :** `GET`  
**Description :** Récupère toutes les réactions associées à un forum donné, triées par date de création (plus récent en premier).

**Exemple de réponse (succès) :**
```json
{
    "data": [
        {
            "id": 1,
            "emoji": ":smile:",
            "position_x": 120,
            "position_y": 300,
            "created_at": "2024-12-08T14:00:00Z"
        }
    ],
    "message": "Reactions were found."
}
```

**Exemple de réponse (échec) :**
```json
{
    "message": "No reactions found."
}
```

---

### 8. Créer une réaction

**URL :** `/reactions/<forum_id>`  
**Méthode :** `POST`  
**Description :** Crée une nouvelle réaction associée à un forum spécifique.

**Requête attendue :**
```json
{
    "emoji_choice": "smile",
    "position_x": 100,
    "position_y": 200
}
```

**Exemple de réponse (succès) :**
```json
{
    "data": {
        "id": 2,
        "emoji": ":smile:",
        "position_x": 100,
        "position_y": 200,
        "created_at": "2024-12-08T14:30:00Z"
    },
    "message": "Reaction successfully created."
}
```

**Exemple de réponse (échec) :**
```json
{
    "message": "Validation error: Emoji is required."
}
```

---

### 9. Supprimer une réaction

**URL :** `/reactions/<reaction_id>`  
**Méthode :** `DELETE`  
**Description :** Supprime une réaction spécifique en fonction de son ID.

**Exemple de réponse (succès) :**
```json
{
    "message": "Reaction has been successfully deleted."
}
```

**Exemple de réponse (échec) :**
```json
{
    "message": "No Reaction found."
}
```

---

## Notes importantes

### Codes de statut HTTP

- **200 OK :** Requête réussie.
- **201 Created :** Objet créé avec succès.
- **400 Bad Request :** Erreur dans la requête (données manquantes ou invalides).
- **404 Not Found :** Objet non trouvé.

### Intégration front-end

- Vérifiez toujours la validité des réponses et gérez les erreurs en affichant les messages inclus dans les réponses.
- Exemple d’utilisation avec Axios (React) :
```javascript
axios.get('/api/mood_choices/')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error.response.data.message);
  });
```


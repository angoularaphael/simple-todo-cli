# Simple Todo CLI - Outil de Gestion de Tâches en Ligne de Commande Python
![Animation Gestion de Tâches en CLI](https://miro.medium.com/v2/resize:fit:1400/1*xIzpUrrVOhl9-PjTLvhBBQ.gif)
[![Licence GitHub](https://img.shields.io/github/license/angoularaphael/simple-todo-cli?style=flat-square)](https://github.com/angoularaphael/simple-todo-cli/blob/main/LICENSE)
[![Étoiles GitHub](https://img.shields.io/github/stars/angoularaphael/simple-todo-cli?style=flat-square)](https://github.com/angoularaphael/simple-todo-cli/stargazers)
[![Forks GitHub](https://img.shields.io/github/forks/angoularaphael/simple-todo-cli?style=flat-square)](https://github.com/angoularaphael/simple-todo-cli/network)
[![Problèmes GitHub](https://img.shields.io/github/issues/angoularaphael/simple-todo-cli?style=flat-square)](https://github.com/angoularaphael/simple-todo-cli/issues)
[![Badge Visiteurs](https://visitor-badge.laobi.icu/badge?page_id=angoularaphael.simple-todo-cli&format=true)](https://github.com/angoularaphael/simple-todo-cli)
## Description
Simple Todo CLI est un outil open-source de gestion de tâches développé en Python, conçu pour fonctionner en ligne de commande. Il permet de gérer efficacement les listes de tâches, les ajouts, les suppressions, les marquages comme complétées et les affichages. Idéal pour les développeurs et utilisateurs cherchant une solution légère et persistante (stockage en JSON) pour organiser leur quotidien.
![Animation Tâches en Terminal](https://i.redd.it/q5ezjc4lh8591.gif)
## Fonctionnalités
- **Ajout de Tâches** : Ajoutez rapidement de nouvelles tâches via la commande.
- **Liste des Tâches** : Affichez toutes les tâches avec leur statut (complétée ou non).
- **Marquage comme Complétée** : Mettez à jour le statut d'une tâche spécifique.
- **Suppression de Tâches** : Retirez des tâches obsolètes.
- **Persistence des Données** : Stockage automatique en fichier JSON pour une utilisation continue.
## Démo
Voici comment fonctionne un peu cet outil.
![Animation Démo Tâches en CLI](https://us1.discourse-cdn.com/cursor1/original/3X/6/f/6f332e6f4431ddfdcf386020e278b4c791a899cb.gif)
## Installation
Pour démarrer avec Simple Todo CLI :
1. Clonez le dépôt :
   ```
   git clone https://github.com/angoularaphael/simple-todo-cli.git
   ```
2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```
3. Lancez l'outil via Python (par exemple, `python todo.py --help` pour voir les commandes).
**Note** : Assurez-vous d'avoir Python 3 installé (version 3.6 ou supérieure recommandée pour une compatibilité optimale).
## Utilisation
- Exécutez les commandes directement en terminal.
- Pour ajouter une tâche : `python todo.py add "Ma tâche importante"`
- Pour lister les tâches : `python todo.py list`
- Pour marquer comme complétée : `python todo.py done 1` (où 1 est l'index de la tâche)
- Pour supprimer : `python todo.py remove 1`
Exemple de code Python basique pour l'ajout d'une tâche (extrait de `todo.py`) :
```python
@cli.command()
@click.argument('task')
def add(task):
    """Ajoute une nouvelle tâche."""
    todos = load_todos()
    todos.append({'task': task, 'done': False})
    save_todos(todos)
    click.echo(f'Tâche ajoutée : {task}')
```
## Contribution
Les contributions sont les bienvenues ! Suivez ces étapes :
1. Forkez le dépôt.
2. Créez une nouvelle branche : `git checkout -b feature/votre-fonctionnalite`.
3. Commitez vos changements : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`.
4. Poussez la branche : `git push origin feature/votre-fonctionnalite`.
5. Ouvrez une Pull Request.
Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails (créez ce fichier si nécessaire).
## Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
## Contact
- Mainteneur : @angoularaphael
- GitHub : [angoularaphael](https://github.com/angoularaphael)
- Email : germainraphaelangoulaonambele@gmail.com
---

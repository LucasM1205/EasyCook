# About EasyCook

<!--EasyCook is a recipe management application developed as part of the "Project I" module in the Bachelor of Science in Business Informatics at the Technical University of Central Hesse. The app was built using the Anvil low-code platform to gain hands-on experience with modern development tools.-->

### Table of Contents
1. Overview
2. Features
3. Technologies
4. Database Structure
5. Server Functions
6. Usage Notes
7. Cloning the App
8. Running the App yourself
9. Reference Documentation
10. Contributors
11. License

## Overview
EasyCook is a user-friendly application that allows users to manage recipes, search by ingredients, and suggest new recipes. The application provides an easy way to favorite recipes and add comments.

### Features
- **Recipe Search**: Users can search for recipes based on keywords or ingredients.
- **Favorites Management**: Users can mark recipes as favorites and manage their favorite recipes.
- **Recipe Suggestions**: Users can suggest new recipes to be added to the application.
- **Comments**: Users can add comments to recipes.
- **Ingredient Management**: Manage and link ingredients to recipes in the backend.
- **Recipe Categorization**: Recipes are categorized by difficulty and visualized accordingly.

### Technologies
- **Anvil**: A low-code platform for web application development.
- **Python 3.10**: For implementing server logic and database operations.
- **SQL Database**: To store recipes, ingredients, favorites, and user information.
- **HTML & CSS**: Used to customize the UI elements and extend the default Anvil roles. Custom styles were applied in the `theme.css` file to enhance the appearance of the app.
- **Free Plan with Anvil**: Used during development, with plans to upgrade to the Hobby Plan before final submission to enable a custom URL.

## Database Structure

The App uses a SQL Database with the following tables:

### Comments (comments)
- **recipe**: Link to `recipes` row
- **user**: Link to `users` row
- **commentText**: string
- **Timestamp**: datetime

### Favorites (favorites)
- **user**: Link to `users` row
- **recipe**: Link to `recipes` row

### Ingredients (ingredients)
- **ingredientID**: number
- **name**: string
- **category**: string
- **unit**: string

### RecipeIngredients (recipeingredients)
- **recipeID**: Link to `recipes` row
- **ingredientID**: Link to `ingredients` row
- **quantity**: number
- **r_ID**: number

### Recipes (recipes)
- **recipeID**: number
- **name**: string
- **description**: string
- **category**: string
- **preparationTime**: number
- **recipePicture**: media
- **preparationSteps**: string
- **favoritesCount**: number
- **difficulty**: string

### Users (users)
- **email**: string
- **enabled**: bool
- **last_login**: datetime
- **password_hash**: string
- **n_password_failures**: number
- **confirmed_email**: bool
- **signed_up**: datetime
- **remembered_logins**: simpleObject
- **email_confirmation_key**: string

## Server Functions

The application contains several server-side functions that handle the core business logic:

- **`search_recipes(keyword)`**: Searches for recipes by keywords in names, descriptions, and ingredients.
- **`add_ingredient(name, category, unit)`**: Adds a new ingredient to the database.
- **`add_recipe(name, description, category, preparation_time)`**: Adds a new recipe to the database.
- **`add_recipe_ingredient(recipe_id, ingredient_id, quantity)`**: Links an ingredient to a recipe.
- **`get_ingredients_for_recipe(recipe_id)`**: Retrieves ingredients for a specific recipe.
- **`get_recipes_by_ingredients(selected_ingredients)`**: Searches for recipes that contain specific ingredients.
- **`get_recipe_details(recipe_id)`**: Retrieves details of a specific recipe, including ingredients, steps, and image.
- **`is_favorite(recipe)`**: Checks if a recipe is in the current user's favorites.
- **`add_to_favorites(recipe)`**: Adds a recipe to the current user's favorites and updates the favorites count.
- **`remove_from_favorites(recipe)`**: Removes a recipe from the current user's favorites and updates the favorites count.
- **`get_popular_recipes(limit=3)`**: Retrieves the recipes with the most favorites.
- **`get_favorite_recipes()`**: Retrieves the favorite recipes of the current user.
- **`add_comment(recipe_id, comment_text)`**: Adds a comment to a recipe.
- **`get_comments_for_recipe(recipe_id)`**: Retrieves comments for a specific recipe.
- **`send_recipe_suggestion(name, description, duration, ingredients, preparation_steps)`**: Sends a recipe suggestion via email to the administrator.

## Usage Notes

To use EasyCook successfully, ensure the database is correctly set up and all dependencies are met. Start the application and log in to access the full features.

## Cloning the App

To clone this app, follow these steps:

1. Go to the [Anvil Editor](https://anvil.works/build?utm_source=github:app_README) (you might need to sign up for a free account) and click on "Clone from GitHub" (underneath the "Blank App" option):

    ![Clone from GitHub](https://anvil.works/docs/version-control-new-ide/img/git/clone-from-github.png)

2. Enter the URL of this GitHub repository. If you're not yet logged in, choose "GitHub credentials" as the authentication method and click "Connect to GitHub".

    ![Clone App from Git modal](https://anvil.works/docs/version-control-new-ide/img/git/clone-app-from-git.png)

3. Finally, click "Clone App".

This app will then be in your Anvil account, ready for you to run it or start editing it! **Any changes you make will be automatically pushed back to this repository, if you have permission!** You might want to [make a new branch](https://anvil.works/docs/version-control-new-ide?utm_source=github:app_README).

## Running the App Yourself

To run the app, find the **Run** button at the top-right of the Anvil editor:

![Run button](https://anvil.works/docs/img/run-button-new-ide.png)

## Reference Documentation

The Anvil reference documentation provides comprehensive information on how to use Anvil to build web applications. You can find the documentation [here](https://anvil.works/docs/overview?utm_source=github:app_README).

If you want to get to the basics as quickly as possible, each section of this documentation features a [Quick-Start Guide](https://anvil.works/docs/overview/quickstarts?utm_source=github:app_README).

## Contributors

- **Lucas Kaczmarczyk**: Lead Developer

## License

This project was developed for the "Project I" module and is not subject to any specific licensing terms.

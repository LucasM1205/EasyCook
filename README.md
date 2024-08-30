# About EasyCook

EasyCook is a recipe management application developed as part of the "Project I" module in the Bachelor of Science in Business Informatics at the Technical University of Central Hesse. The app was built using the Anvil low-code platform to gain hands-on experience with modern development tools.

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

### Overview
EasyCook is a user-friendly application that allows users to manage recipes, search by ingredients, and suggest new recipes. The application provides an easy way to favorite recipes and add comments.

### Features
- **Recipe Search**: Users can search for recipes based on keywords or ingredients.
- **Favorites Management**: Users can mark recipes as favorites and manage their favorite recipes.
- **Recipe Suggestions**: Users can suggest new recipes to be added to the application.
- **Comments**: Users can add comments to recipes.
- **Ingredient Management**: Manage and link ingredients to recipes.
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

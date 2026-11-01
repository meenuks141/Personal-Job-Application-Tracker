# Obstacle Log – Personal Job Application Tracker

## 1. Data Persistence

Challenge: Application data would be lost when the program terminated.

Solution: Used Python’s JSON module to store and retrieve application records from a JSON file.

## 2. Status Validation

Challenge: Invalid application statuses could affect the summary.

Solution: Implemented status validation using a predefined list of valid statuses: Applied, Interview, Selected and Rejected.

## 3. Searching Applications

Challenge: Searching required matching company names and statuses accurately.

Solution: Implemented case-insensitive searching to make the tracker more user-friendly.

## 4. Updating Application Status

Challenge: Application statuses needed to be updated as candidates progressed through the recruitment process.

Solution: Created an update function that identifies applications using company and role names.

## 5. Generating Reports

Challenge: Application information needed to be presented in an organized format.

Solution: Used Python file handling to generate a text report containing all applications, status counts and current interview details.

## Conclusion

Successfully developed a Personal Job Application Tracker using Python, JSON and file handling. The project helped me understand functions, lists, dictionaries, data persistence and basic data analysis.
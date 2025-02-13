class GenerateOutput:
    def __init__(self) -> None:
        pass

    def generate_output(self) -> dict:
         # Here you would include the logic to initialize the test
        context = {
            "quizzes": [
                {
                "test_count": 1,
                "pass_marks": 50,
                "total_marks": 100,
                "title": "Math Quiz",
                "description": "A quiz to test your mathematical knowledge.",
                "questions": [
                    {
                    "question": "What is 2 + 2?",
                    "options": [
                        "3",
                        "4",
                        "5",
                        "6"
                    ],
                    "total_marks": 10
                    },
                    {
                    "question": "What is 5 * 6?",
                    "options": [
                        "30",
                        "35",
                        "40",
                        "25"
                    ],
                    "total_marks": 10
                    }
                ]
                },
                {
                "test_count": 2,
                "pass_marks": 60,
                "total_marks": 120,
                "title": "Science Quiz",
                "description": "A quiz on basic science concepts.",
                "questions": [
                    {
                    "question": "What is the chemical symbol for water?",
                    "options": [
                        "H2O",
                        "CO2",
                        "O2",
                        "H2"
                    ],
                    "total_marks": 10
                    },
                    {
                    "question": "What is the powerhouse of the cell?",
                    "options": [
                        "Nucleus",
                        "Mitochondria",
                        "Ribosome",
                        "Endoplasmic Reticulum"
                    ],
                    "total_marks": 10
                    }
                ]
                }
            ],
            "pass_mark": 70,
            "total_mark": 220,
            "test_count": 2,
            "db_path": "/path/to/database"
            }
        return context
    

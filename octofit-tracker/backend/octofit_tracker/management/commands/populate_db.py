from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Activity, Team, Leaderboard, Workout
import datetime


class Command(BaseCommand):
    help = 'Populate the database with initial test data for OctoFit Tracker'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users_data = [
            {'username': 'thundergod', 'email': 'thor@mergington.edu', 'password': 'password123'},
            {'username': 'magicschoolbus', 'email': 'frizzle@mergington.edu', 'password': 'password123'},
            {'username': 'octofitpro', 'email': 'octo@mergington.edu', 'password': 'password123'},
            {'username': 'speedster', 'email': 'flash@mergington.edu', 'password': 'password123'},
            {'username': 'ironclad', 'email': 'iron@mergington.edu', 'password': 'password123'},
        ]
        users = []
        for data in users_data:
            user = User.objects.create(**data)
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')

        # Create activities
        activities_data = [
            {'user': users[0], 'activity_type': 'Running', 'duration': 30, 'date': datetime.date(2024, 1, 10)},
            {'user': users[1], 'activity_type': 'Cycling', 'duration': 45, 'date': datetime.date(2024, 1, 11)},
            {'user': users[2], 'activity_type': 'Swimming', 'duration': 60, 'date': datetime.date(2024, 1, 12)},
            {'user': users[3], 'activity_type': 'Strength Training', 'duration': 40, 'date': datetime.date(2024, 1, 13)},
            {'user': users[4], 'activity_type': 'Yoga', 'duration': 50, 'date': datetime.date(2024, 1, 14)},
            {'user': users[0], 'activity_type': 'Walking', 'duration': 25, 'date': datetime.date(2024, 1, 15)},
        ]
        for data in activities_data:
            activity = Activity.objects.create(**data)
            self.stdout.write(f'Created activity: {activity.activity_type} for {activity.user.username}')

        # Create teams
        team_a = Team.objects.create(name='The Avengers')
        team_a.members.add(users[0], users[1], users[2])
        self.stdout.write(f'Created team: {team_a.name}')

        team_b = Team.objects.create(name='The Guardians')
        team_b.members.add(users[3], users[4])
        self.stdout.write(f'Created team: {team_b.name}')

        # Create leaderboard entries
        leaderboard_data = [
            {'user': users[0], 'score': 450},
            {'user': users[1], 'score': 390},
            {'user': users[2], 'score': 520},
            {'user': users[3], 'score': 310},
            {'user': users[4], 'score': 410},
        ]
        for data in leaderboard_data:
            entry = Leaderboard.objects.create(**data)
            self.stdout.write(f'Created leaderboard entry: {entry.user.username} - {entry.score}')

        # Create workouts
        workouts_data = [
            {
                'name': '5K Run',
                'description': 'A moderate-intensity 5 kilometer run to build cardiovascular endurance.',
                'duration': 30,
            },
            {
                'name': 'Full Body Strength',
                'description': 'A comprehensive strength training session targeting all major muscle groups.',
                'duration': 45,
            },
            {
                'name': 'Yoga Flow',
                'description': 'A relaxing yoga session focused on flexibility and mindfulness.',
                'duration': 40,
            },
            {
                'name': 'HIIT Cardio',
                'description': 'High-intensity interval training to maximize calorie burn in minimal time.',
                'duration': 25,
            },
            {
                'name': 'Swimming Laps',
                'description': 'A swimming workout alternating between freestyle and backstroke.',
                'duration': 50,
            },
        ]
        for data in workouts_data:
            workout = Workout.objects.create(**data)
            self.stdout.write(f'Created workout: {workout.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with initial data!'))

from django.shortcuts import render
from .models import GuessingGame
import random

def home(request):
    game, created = GuessingGame.objects.get_or_create(pk=1, defaults={'secret_number': random.randint(1, 10)})

    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        if guess == game.secret_number:
            result = "Congratulations! You guessed it right."
            game.attempts += 1
            game.save()
        else:
            if game.attempts < game.max_attempts - 1:
                result = "Try again! Wrong guess."
                game.attempts += 1
                game.save()
            else:
                result = f"Game over! The number was {game.secret_number}."
                game.delete()
                return render(request, 'game_over.html', {'result': result})

        return render(request, 'home.html', {'result': result})
    return render(request, 'home.html')
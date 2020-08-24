import eel
import parsingweather

eel.init('web')
@eel.expose
def get_weather(place):
    try:
        answer = parsingweather.parse(place.lower())[0]
        answer1 = parsingweather.parse(place.lower())[1]
        result = answer1 + answer[0] + ' ' + answer[1] + ' ' + answer[2] + 'Минимальная температура: ' + answer[
            3] + 'Максимальная температура: ' + answer[4]
    except IndexError:
        return "Такого города нет"
    return result
eel.start('main.html', size=(700, 700))

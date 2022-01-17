"""Restaurant rating lister."""


# put your code here
def get_scores():
    scores_dict = {}
    scores = open("scores.txt")

    for line in scores:
        line = line.rstrip()
        resturant, rating = line.split(":")
        scores_dict[resturant] = int(rating)

    return scores_dict


def add_restaurant(scores):
    print("Please add a rating for a resturant!")
    restaurant = input("Restaurant Name: ")
    rating = int(input("Rating: "))

    scores[restaurant] = rating


def print_sorted_scores(scores):
    for resturant, rating in sorted(scores.items()):
        print(f"{resturant} is rated {rating}.")


scores = get_scores()

add_restaurant(scores)

print_sorted_scores(scores)
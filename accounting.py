#*Someone counted up the different types of melons that were sold.
#*Someone calculated the revenue from those melon tallies.
#*Someone separated sales into online sales and phone sales.
#*Someone produced a fancy report to summarize the information for our CEO

def count_melons_sold():
    """Counts number of melons sold by type of melon"""

    # create dictionary with melon type (key) and number sold (value)
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}

    # open file
    f = open("orders_by_type.csv")

    # read file
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        # count melons sold per type (key/value pair)
        melon_tallies[melon_type] += melon_count
    f.close()

    # calculate melon revenue
    calculate_revenue(melon_tallies)


def calculate_revenue(melon_tallies):
    """Calculates total revenue of all melons sold, for all types"""

    # create dictionary with melon type (key) and melon price (value)
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

    # calculate revenue based on number of melons sold
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at $%0.2f each for a total of $%0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)


def separate_sales():
    """Separate sales revenue based on online or phone"""

    # open and read sales file
    f = open("orders_with_sales.csv")
    sales = [0, 0]
    for line in f:
        data = line.split(",")

        # separate online sales and phone sales
        if data[1] == "0":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])

    print "Salespeople generated $%0.2f in revenue." % sales[1]
    print "Internet sales generated $%0.2f in revenue." % sales[0]

    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"


def print_horizontal_rule():
    """Prints a uniform horizontal rule to separate information in report"""

    print "******************************************"


def main():
    
    print_horizontal_rule()

    # count number of melons sold by type and calculate revenue
    count_melons_sold()

    print_horizontal_rule()

    # Separate sales information by internet vs phone
    separate_sales()
        
    print_horizontal_rule()


if __name__ == "__main__":
    main()

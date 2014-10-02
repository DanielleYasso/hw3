#*Someone counted up the different types of melons that were sold.
#*Someone calculated the revenue from those melon tallies.
#*Someone separated sales into online sales and phone sales.
#*Someone produced a fancy report to summarize the information for our CEO

def main():
    print "******************************************"

    # open file
    f = open("orders_by_type.csv")

    # create dictionary with melon type (key) and number sold (value)
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
    
    # read file
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        # count melons sold per type (key/value pair)
        melon_tallies[melon_type] += melon_count
    f.close()

    # create dictionary with melon type (key) and melon price (value)
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

    # calculate revenue based on number of melons sold
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)

    print "******************************************"

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

    print "Salespeople generated %0.2f in revenue." % sales[1]
    print "Internet sales generated %0.2f in revenue." % sales[0]

    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"
        
    print "******************************************"


if __name__ == "__main__":
    main()

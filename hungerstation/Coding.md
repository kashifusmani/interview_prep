## Code

### Case:

We have a food delivery application that connects between a customer, a restaurant.

The customer can order any food, and the system will send the order to the restaurant , then the system will summarize the order and send the result to the customer.

When the order is confirmed, the Order will be paid using user wallet

**The Main Objects:**

***Entity:***

- Customer
- MenuItem
- Restaurant
- RestaurantMenu
- Order
- OrderDetail

***Services:***

- OrderService
- PaymentService

&nbsp;

## Problem Statement:

- System supports multiple payment methods (wallet, cash and credit card)
    - We can choose any payment we want to use
    - Also support for split payment using available payment methods

- Every weekend, every customer will get a 10% discount.
    - Customer will get additional 5% if the is age more than 50 years old
    - Customer will get additional 5% if they order on their birthday

&nbsp;

## Todo:

- **Design the solution for problem statements above**
- **Use best practice approach to implement the solution (Design Pattern, Scalability, KISS, etc)**

<p>&nbsp;</p>

**Golang Skeleton**

```golang
// customer
interface Customer {
    name string
    walletAmount int
}

//menu item
interface MenuItem {
    name string
}

// restaurant menu
interface RestaurantMenu {
    menuItem MenuItem
    price int
}

// restaurant
interface Restaurant {
    name string
    restaurantMenus []RestaurantMenu
}

// order
interface Order {
    orderNumber string
    restaurant Restaurant
    customer Customer
    status string
    orderDetail OrderDetail
}

// order detail
interface OrderDetail {
    orderNumber string
    item string
    quantity int
    itemPrice int
    totalPrice int
}

// methods to pay order
func (o Order) payOrder() error{
    //Pay Order
}
```
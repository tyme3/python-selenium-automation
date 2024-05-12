Feature: Adding an item to the cart

  Scenario Outline: Add an item to the cart
    Given I am on the Target website
    When I search for "<keyword>"
    When I add the first item to my cart
    Then I should see the "<expected_item>" in my cart

    Examples:
      | keyword   | expected_item |
      | laptop    | laptop        |
      | orange    | orange        |
      | lemon     | lemon         |


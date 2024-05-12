Feature: Verify color selection on Target product page

  Scenario: Verify color selection functionality on Target product page
    Given I navigate to the Target product page
    When I loop through color options and verify each color selection
    Then I should see that each color has been selected

# Created by Dimitri at 5/10/2024
Feature: Verify Empty Cart Message

  Scenario: Verify "Your cart is empty" message
   Given Open Target main page
   When  Click on the Cart icon
   Then  Verify "Your cart is empty" message is shown
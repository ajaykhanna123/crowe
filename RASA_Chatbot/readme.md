# Implementation 

## Entities usage:
### Made use of entities and roles to fetch dates(roles as 'to' and 'from') from text and then pass data to action where dates are converted into datetime using python
### Made use of lookup table to fetch states names in the text and then pass them as entities to actions
### To fetch the pattern of date made use of RegexEntityExtractor and then pass it in the intents

## action
### Made custom actions  to implement the functionality of APIs in order to perform following actions:
### get confirmed cases b/w particular dates and for a particular date .
### get confirmed cases of states together and separately

##stories

### adding the flow in stories



## Sample of input and responses by the bot

  Bot loaded. Type a message and press enter (use '/stop' to exit):

  Your input ->  hi                                                                                                                                 
  Hey! How are you?
  
  Your input ->  covid cases in punjab                                                                                                              
  Total Confirmed cases for punjab is 117509634
  
  Your input ->  total cases in delhi                                                                                                               
  Total Confirmed cases for delhi is 329043520
  
  Your input ->  total cases in delhi and punjab                                                                                                    
  Total Confirmed cases for punjab is 117509634
  Total Confirmed cases for delhi is 329043520
  
  Your input ->  total cases in delhi and punjab together                                                                                           
  Total confirmed cases for states  punjab , delhi altogether is 446553154
  
  Your input ->  total cases from 20 dec 2020 to 24 dec 2020                                                                                        
  Total cases b/w  20 dec 2020 and 24 dec 2020 are 50384743
  
  Your input ->  total cases for data 20 dec 2020                                                                                                   
  Total cases on date 20 dec 2020 are 10031223
  
  Your input ->  total cases from 20 dec 2020 to 10 dec 2020                                                                                        
  Invalid date format ..try with different one!



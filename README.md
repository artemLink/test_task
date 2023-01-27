# test_task

<h1>URLS<h1>

  POST api/v1/token/ - Get JWT token
  
  GET api/v1/taglist/ - Get a list of tags
  
  GET api/v1/event/<int:pk>/ - Get one event by id
  
  DELETE api/v1/delete-event/<int:pk>/ - Delete event
  
  PATCH api/v1/update-event/<int:pk>/ - Update event
  
  GET api/v1/allevent/ - View all events
  
  POST api/v1/create-event/ - Create event
  
  
  Model Event:
  
  - time (Automatically indicated)
  - user (Gets from JWT token)
  - event_type ('possible', 'random','impossible')
  - description
  - category ('info', 'attention','alarm')
  - tags
  
  Model Tag:
  
  - name

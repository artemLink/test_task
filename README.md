# test_task

<h1>URLS</h1>

  <b>POST</b> api/v1/token/ - Get JWT token
  
  <b>GET</b> api/v1/taglist/ - Get a list of tags
  
  <b>GET</b> api/v1/event/<int:pk>/ - Get one event by id
  
  <b>DELETE</b> api/v1/delete-event/<int:pk>/ - Delete event
  
  <b>PATCH</b> api/v1/update-event/<int:pk>/ - Update event
  
  <b>GET</b> api/v1/allevent/ - View all events
  
  <b>POST</b> api/v1/create-event/ - Create event
  
  
  Model Event:
  
  - time (Automatically indicated)
  - user (Gets from JWT token)
  - event_type ('possible', 'random','impossible')
  - description
  - category ('info', 'attention','alarm')
  - tags
  
  Model Tag:
  
  - name

<!DOCTYPE html>

<html>
<head>
<title>Update Dragon</title>
</head>
<form action='upsert_dragon', method='POST'>
<p>Name: 
  <input type='text' name='dragon_name' value="{{dragon['name']}}">
<p>UPP:
  <input type='text' name='dragon_upp' value="{{dragon['upp']}}"> 
<p>
% for k, v in dragon['skills'].iteritems():
  {{ k }}-{{ v }}  
% end
<input type='submit' value='Update'>
</form>

</body>
</html>

<!DOCTYPE html>

<html>
<head>
<title>Dragon Selection</title>
</head>
</body>
<p>{{dragon['name']}}
 {{ dragon['upp'] }}
 [{{ dragon['gender'] }}]
 Age: {{ dragon['age'] }}
<p>
% for k, v in dragon['skills'].iteritems():
  {{ k }}-{{ v }}  
% end

<form action='upsert_dragon', method='POST'>
<input type='text' name='search_name' value="{{dragon['name']}}">
<input type='submit' value='Update?'>
</form>
</body>
</html>

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
</body>
</html>

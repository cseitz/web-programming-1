<html>
<body>
<h2>Hello, {{name}}!</h2>
<hr>
<ul>
% for item in items:
    <li>{{item['note']}}</li>
% end
</ul>
</body>
</html>
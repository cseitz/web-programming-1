const express = require('express');
const app = express();

app.use(express.static(__dirname));

const { readFile, writeFile } = require('fs/promises');
app.post('/api/reviews.json', express.json(), async (req, res) => {
    const {
        path,
        body: newReviews
    } = req;
    const data = await readFile(__dirname + path, 'utf8');
    const reviews = JSON.parse(data.length > 0 ? data : '[]');
    for (const review of newReviews) reviews.push(review);
    await writeFile(__dirname + path, JSON.stringify(reviews));
    res.status(200).json(reviews);
})

app.listen(8888);
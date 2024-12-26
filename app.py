from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ideas_text = request.form['ideas']
        ideas = [idea.strip() for idea in ideas_text.strip().split('\n') if idea.strip()]
        session['ideas_to_sort'] = ideas
        session['sorted_ideas'] = []
        session['current_insertion'] = None
        session['left'] = None
        session['right'] = None
        return redirect(url_for('insert'))
    return render_template('index.html')


@app.route('/insert')
def insert():
    ideas_to_sort = session.get('ideas_to_sort', [])
    if not ideas_to_sort:
        # All ideas have been sorted
        return redirect(url_for('result'))
    else:
        # Take the next idea to insert
        current_idea = ideas_to_sort.pop(0)
        session['ideas_to_sort'] = ideas_to_sort
        session['current_insertion'] = current_idea
        # Start binary search on sorted_ideas
        sorted_ideas = session.get('sorted_ideas', [])
        if not sorted_ideas:
            # First idea, just insert it
            sorted_ideas.append(current_idea)
            session['sorted_ideas'] = sorted_ideas
            return redirect(url_for('insert'))
        else:
            # Initialize binary search indices
            session['left'] = 0
            session['right'] = len(sorted_ideas)
            return redirect(url_for('binary_compare'))


@app.route('/binary_compare', methods=['GET', 'POST'])
def binary_compare():
    if request.method == 'POST':
        choice = request.form['choice']
        current_idea = session['current_insertion']
        sorted_ideas = session['sorted_ideas']
        left = session['left']
        right = session['right']
        mid = (left + right) // 2
        if choice == 'current':
            # User prefers current_idea over mid_idea
            right = mid
        else:
            # User prefers mid_idea over current_idea
            left = mid + 1
        session['left'] = left
        session['right'] = right
        if left >= right:
            # Insert current_idea at position left
            sorted_ideas.insert(left, current_idea)
            session['sorted_ideas'] = sorted_ideas
            # Proceed to the next idea
            return redirect(url_for('insert'))
        else:
            # Continue binary search
            return redirect(url_for('binary_compare'))
    else:
        current_idea = session['current_insertion']
        sorted_ideas = session['sorted_ideas']
        left = session['left']
        right = session['right']
        if left >= right:
            # Insert current_idea at position left
            sorted_ideas.insert(left, current_idea)
            session['sorted_ideas'] = sorted_ideas
            # Proceed to the next idea
            return redirect(url_for('insert'))
        else:
            # Compare current_idea with the middle idea
            mid = (left + right) // 2
            mid_idea = sorted_ideas[mid]
            return render_template('compare.html', idea1=current_idea, idea2=mid_idea)


@app.route('/result')
def result():
    sorted_ideas = session.get('sorted_ideas', [])
    return render_template('result.html', ideas=sorted_ideas)


if __name__ == '__main__':
    app.run(debug=True)

## 1. Git conflict
**Task:**
- Describe in pseudocode(Git CLI) resolving conflict in merge request FBranch -> master.

**Solution:**
1. First, checkout the "master" branch:
```bash
git checkout master
```

2. Then, pull any changes that have been made to the "master" branch 
since the creation of the merge request:
```bash
git pull origin master
```

3. Next, checkout the "FBranch" branch:
```bash
git checkout FBranch
```

4. Merge the latest changes from "master" into the "FBranch" branch:
```bash
git merge master
```

5. If there are any conflicts, Git will inform you which files have conflicts. 
Open the conflicted files in a text editor and look for the conflict markers, which look like this:
```
<<<<<<< HEAD
Code from the current branch (FBranch)
=======
Code from the incoming branch (master)
>>>>>>> master
```

6. Edit the file to remove the conflict markers and make any necessary changes to resolve the conflicts.

7. After editing the file, stage it for commit:
```bash
git add <filename>
```

8. Once all conflicts have been resolved, commit the changes with a message describing the conflict resolution:
```bash
git commit -m "Resolved conflicts in merge request FBranch -> master"
```

9. Finally, push the changes to the remote repository:
```bash
git push origin FBranch
```

## 2. Get last price
**Task:**
- Describe in pseudocode(Python script), how you can get last price from 
this page: https://www.investing.com/equities/apple-computer-inc.

**Solution:**
1. First of all, I check if the API is available (it is, but the site 
is protected from scraping)
2. The next step that should be taken in such a case is to contact the 
website owner and ask if it is possible and how best to get the necessary data.
3. You can bypass step 2 using the Selenium framework, but this is still not the
best solution.
4. In the case of the test task, I neglect step 2. Using the third-party 
**investiny** library, I get the necessary data (**[scraper](scraper.py)** file).

## 3. SQL
**Task:**
- Give short answers to the following questions (SQL/PostgreSQL) basing
on a SQL query below:

3.1. Which indexes can improve performance of the query?  
**Answer:** There several types of indexes, that can significantly improve
performance of the query:
- Primary Key Index
- Unique Index
- B-Tree Index
- Hash Index
- GiST Index

3.2. How can you check efficacy/performance of this query?
What indicators should you pay attention to? 
**Answer:** To check the performance of a query, I can use the 
PostgreSQL "EXPLAIN" statement. The second way to use "EXPLAIN" is to run
"EXPLAIN ANALYZE" instead. The most important indicator of an output is a
"QUERY PLAN" section.

3.3. Suggest a way to get additional information from last_visit - 
not only user_visit.created_at, but also user_visit.url, for example.

```sql
SELECT
    u.id,
    (
        SELECT created_at
        FROM user_visit
        WHERE user_id = u.id
        ORDER BY created_at DESC
        LIMIT 1
    ) AS last_visit
FROM user u
WHERE
    email IN (...) AND
    created_at > TIMESTAMP
```

**Answer:** 
```sql
SELECT
    u.id,
    uv.last_visit,
    uv.url
FROM user u
LEFT JOIN (
    SELECT user_id, created_at AS last_visit, url
    FROM user_visit
    WHERE (user_id, created_at) IN (
        SELECT user_id, MAX(created_at)
        FROM user_visit
        GROUP BY user_id
    )
) uv ON u.id = uv.user_id
WHERE
    email IN (...) AND
    created_at > TIMESTAMP
```

```sql
SELECT t1.server, t1.opponent, AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point, COUNT(*) as total_matches_played FROM default.servetimesdb t1 JOIN default.eventtimesdb t2 ON t1.id = t2.id GROUP BY t1.server, t1.opponent ORDER BY total_matches_played DESC LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent, AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point, COUNT(*) as total_matches_played FROM default.servetimesdb t1 JOIN default.eventtimesdb t2 ON t1.id = t2.id GROUP BY t1.server, t1.opponent ORDER BY total_matches_played DESC LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent, AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point, COUNT(*) as total_matches_played FROM default.servetimesdb t1 JOIN default.eventtimesdb t2 ON t1.id = t2.id GROUP BY t1.server, t1.opponent ORDER BY total_matches_played DESC LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent, AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point, COUNT(*) as total_matches_played FROM default.servetimesdb t1 JOIN default.eventtimesdb t2 ON t1.id = t2.id GROUP BY t1.server, t1.opponent ORDER BY total_matches_played DESC LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent, AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point, COUNT(*) as total_matches_played FROM default.servetimesdb t1 JOIN default.eventtimesdb t2 ON t1.id = t2.id GROUP BY t1.server, t1.opponent ORDER BY total_matches_played DESC LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=76), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=64), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.47826086956522, total_matches_played=46), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.59090909090909, total_matches_played=44), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.657894736842106, total_matches_played=38), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=36), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=32), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=29.0, total_matches_played=32), Row(server='Pablo Andujar', opponent='Philipp Kohlschreiber', avg_seconds_before_next_point=30.93548387096774, total_matches_played=31), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.774193548387096, total_matches_played=31)]
```


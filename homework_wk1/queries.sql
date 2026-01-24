-- Verify the data in the tables
SELECT *
FROM green_taxi_trips ;

SELECT *
FROM public.green_taxi_zones;

-- Question 3 Counting Short Trips in November 2025

SELECT count(lpep_pickup_datetime)
FROM green_taxi_trips
WHERE DATE(lpep_pickup_datetime) BETWEEN '2025-11-01' and '2025-11-30'
AND trip_distance <= 1;

-- Question 4 Longest Trip for Each Day
SELECT DATE(lpep_pickup_datetime) Date_with_the_longest_trip
FROM green_taxi_trips
WHERE trip_distance = (
SELECT  max(trip_distance)
FROM green_taxi_trips
WHERE trip_distance < 100);

-- Question 5. Biggest pickup zone by total trip amount on November 18, 2025
SELECT gz."Zone",
		SUM(total_amount) AS trip_amount
FROM green_taxi_trips gt
JOIN green_taxi_zones gz
ON gt."PULocationID" = gz."LocationID"
WHERE DATE(gt.lpep_pickup_datetime) = '2025-11-18'
GROUP BY gz."Zone"
ORDER BY trip_amount DESC
LIMIT 1;


SELECT gt.lpep_pickup_datetime,puz."Zone", doz."Zone", gt.tip_amount
FROM green_taxi_trips gt
JOIN green_taxi_zones puz
ON gt."PULocationID" = puz."LocationID"
JOIN green_taxi_zones doz
ON gt."DOLocationID" = doz."LocationID"
WHERE puz."Zone" = 'East Harlem North'
AND DATE(gt.lpep_pickup_datetime) BETWEEN '2025-11-01' AND '2025-11-30'
ORDER BY  gt.tip_amount DESC
LIMIT 1;


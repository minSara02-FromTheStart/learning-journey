function calculateMean(arr){

    let sum = 0;

    for(let i = 0; i < arr.length; i++){
        sum += arr[i];
    }

    return (sum / arr.length).toFixed(2);
}

function calculateMedian(arr){

    let middle = Math.floor(arr.length / 2);

    return arr[middle];
}

function showNormal(){

    let data = [70,75,80,85,90];

    document.getElementById("numberBox").innerText =
        data.join(", ");

    document.getElementById("meanText").innerText =
        "Mean = " + calculateMean(data);

    document.getElementById("medianText").innerText =
        "Median = " + calculateMedian(data);

    document.getElementById("explanation").innerText =
        "Both mean and median are similar because there is no extreme value.";
}

function showOutlier(){

    let data = [70,75,80,85,300];

    document.getElementById("numberBox").innerText =
        data.join(", ");

    document.getElementById("meanText").innerText =
        "Mean = " + calculateMean(data);

    document.getElementById("medianText").innerText =
        "Median = " + calculateMedian(data);

    document.getElementById("explanation").innerText =
        "The outlier heavily changes the mean, but the median stays stable.";
}
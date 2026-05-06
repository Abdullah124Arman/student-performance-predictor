package com.example.studentperformanceapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;
import okhttp3.ResponseBody;

public class MainActivity extends AppCompatActivity {

    private EditText etAttendance, etInternal1, etInternal2, etAssignment;
    private TextView tvResult;
    private ProgressBar progressBar;
    private Button btnPredict;

    private final OkHttpClient client = new OkHttpClient();


    private static final String PREDICT_URL = "https://student-performance-predictor-op84.onrender.com/predict";
    public static final MediaType JSON
            = MediaType.parse("application/json; charset=utf-8");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etAttendance = findViewById(R.id.etAttendance);
        etInternal1 = findViewById(R.id.etInternal1);
        etInternal2 = findViewById(R.id.etInternal2);
        etAssignment = findViewById(R.id.etAssignment);
        tvResult = findViewById(R.id.tvResult);
        progressBar = findViewById(R.id.progressBar);
        btnPredict = findViewById(R.id.btnPredict);

        btnPredict.setOnClickListener(v -> sendPredictionRequest());
    }

    private void sendPredictionRequest() {
        // Read input values
        String attStr = etAttendance.getText().toString().trim();
        String int1Str = etInternal1.getText().toString().trim();
        String int2Str = etInternal2.getText().toString().trim();
        String assignStr = etAssignment.getText().toString().trim();

        if (attStr.isEmpty() || int1Str.isEmpty() || int2Str.isEmpty() || assignStr.isEmpty()) {
            Toast.makeText(this, "Please fill all fields", Toast.LENGTH_SHORT).show();
            return;
        }

        double attendance, internal1, internal2, assignment;

        try {
            attendance = Double.parseDouble(attStr);
            internal1 = Double.parseDouble(int1Str);
            internal2 = Double.parseDouble(int2Str);
            assignment = Double.parseDouble(assignStr);
        } catch (NumberFormatException e) {
            Toast.makeText(this, "Please enter valid numbers", Toast.LENGTH_SHORT).show();
            return;
        }


        // Validation
        if (attendance < 0 || attendance > 100) {
            etAttendance.setError("Attendance must be 0-100");
            return;
        }

        if (internal1 < 0 || internal1 > 20) {
            etInternal1.setError("Internal 1 must be between 0 and 20");
            return;
        }

        if (internal2 < 0 || internal2 > 20) {
            etInternal2.setError("Internal 2 must be between 0 and 20");
            return;
        }

        if (assignment < 0 || assignment > 20) {
            etAssignment.setError("Assignment must be between 0 and 20");
            return;
        }

        // Show loading state
        progressBar.setVisibility(View.VISIBLE);
        btnPredict.setEnabled(false);
        tvResult.setText("Predicting...");

        // Create JSON body
        JSONObject json = new JSONObject();
        try {
            json.put("attendance", attendance);
            json.put("internal1", internal1);
            json.put("internal2", internal2);
            json.put("assignment", assignment);
        } catch (JSONException e) {
            e.printStackTrace();
            hideLoading();
            return;
        }

        RequestBody body = RequestBody.create(json.toString(), JSON);

        Request request = new Request.Builder()
                .url(PREDICT_URL)
                .post(body)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
                runOnUiThread(() -> {
                    hideLoading();
                    tvResult.setText("Connection failed. Check if server is running.");
                    Toast.makeText(MainActivity.this, "Error: " + e.getMessage(), Toast.LENGTH_LONG).show();
                });
            }

            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
                try (ResponseBody responseBody = response.body()) {
                    if (!response.isSuccessful()) {
                        runOnUiThread(() -> {
                            hideLoading();
                            tvResult.setText("Server Error: " + response.code());
                        });
                        return;
                    }

                    if (responseBody != null) {
                        String content = responseBody.string();
                        JSONObject resJson = new JSONObject(content);
                        final String prediction = resJson.optString("prediction", "Unknown");
                        final String confidence = resJson.optString("confidence", "0%");


                        int confValue = 0;

                        try {
                            confValue = (int) Double.parseDouble(confidence.replace("%", ""));
                        } catch (Exception e) {
                            confValue = 0;
                        }
                        final String riskLevel;

                        if (prediction.equalsIgnoreCase("Fail")) {
                            riskLevel = "HIGH";
                        } else if (confValue >= 85) {
                            riskLevel = "LOW";
                        } else {
                            riskLevel = "MEDIUM";
                        }

                        runOnUiThread(() -> {
                            hideLoading();

// Convert confidence string to number


// Show result
                            tvResult.setText(
                                    "STUDENT PERFORMANCE RESULT\n\n" +
                                            prediction.toUpperCase() +
                                            "\n\nConfidence: " + confidence +
                                            "\nRisk Level: " + riskLevel
                            );

// Set text color
                            int color = prediction.equalsIgnoreCase("Pass") ?
                                    android.R.color.holo_green_dark :
                                    android.R.color.holo_red_dark;

                            tvResult.setTextColor(
                                    ContextCompat.getColor(MainActivity.this, color)
                            );

                            tvResult.setTextSize(20);
                            tvResult.setPadding(20,20,20,20);
                        });
                    }
                } catch (JSONException e) {
                    runOnUiThread(() -> {
                        hideLoading();
                        tvResult.setText("Error parsing response");
                    });
                }
            }

        });
            }
            private void hideLoading() {
                progressBar.setVisibility(View.GONE);
                btnPredict.setEnabled(true);
            }
        }

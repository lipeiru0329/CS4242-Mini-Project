package com.example.user.cs4242;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.github.mikephil.charting.charts.PieChart;
import com.github.mikephil.charting.data.PieDataSet;
import com.github.mikephil.charting.data.PieEntry;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    public int totalChoose = 0;
    public int nowChoose = 0;
    TextView warning;
    List<String> hints = new ArrayList<String>();
    TextView now;
    TextView total;
    Button next;
    EditText password;
    EditText username;
    CheckBox checkBoxTwitter;
    CheckBox checkBoxFacebook;
    private static String TAG = "Result";
    private float[] data = {25.3f, 23.5f, 54.6f, 33.3f, 23.1f};
    private String[] name = {"a", "b", "c", "d", "e"};
    PieChart pieChart;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(TAG, "onCreate: Piechart");
        setContentView(R.layout.activity_main);
        pieChart=findViewById(R.id.Piechart);
        now = findViewById(R.id.now);
        total = findViewById(R.id.total);
        next = findViewById(R.id.next);
        password = findViewById(R.id.password);
        username = findViewById(R.id.username);
        warning = findViewById(R.id.warning);
        checkBoxTwitter = findViewById(R.id.checkBoxTwitter);
        checkBoxFacebook = findViewById(R.id.checkBoxFacebook);
        username.setVisibility(View.INVISIBLE);
        password.setVisibility(View.INVISIBLE);
        warning.setVisibility(View.VISIBLE);
        checkBoxTwitter.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                checkBoxHandler(compoundButton.getText().toString(), b);
                updateUI();
            }
        });

        checkBoxFacebook.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                checkBoxHandler(compoundButton.getText().toString(), b);
                updateUI();
            }
        });

    }

    private void checkBoxHandler(String a, boolean b) {
        if (b) {
            Toast.makeText(getApplicationContext(), "You choose " + a,
                    Toast.LENGTH_SHORT).show();
            hints.add(a+ " Username:");
            Collections.sort(hints);
            totalChoose++;
            Log.i("Hints", hints.toString());
        } else {
            Toast.makeText(getApplicationContext(), "You do not choose " + a,
                    Toast.LENGTH_LONG).show();
            hints.remove(hints.indexOf(a + " Username:"));
            Collections.sort(hints);
            totalChoose--;
            Log.i("Hints", hints.toString());
        }
    }

    private void updateUI() {
        total.setText(Integer.toString(totalChoose));
        now.setText(totalChoose > 0 ? "1" : "0");
        if (totalChoose == 0) {
            username.setEnabled(false);
            password.setEnabled(false);
            username.setVisibility(View.INVISIBLE);
            password.setVisibility(View.INVISIBLE);
            warning.setVisibility(View.VISIBLE);
        } else {
            username.setEnabled(true);
            password.setEnabled(true);
            username.setVisibility(View.VISIBLE);
            password.setVisibility(View.VISIBLE);
            warning.setVisibility(View.INVISIBLE);
        }
    }
    private void makePieChart(String description) {
        pieChart.setContentDescription(description);
        pieChart.enableScroll();
        pieChart.setRotationEnabled(true);
        pieChart.setHoleRadius(25f);
        addData(pieChart);
    }

    private void addData(PieChart pieChart) {
        ArrayList<PieEntry> pieEntries = new ArrayList<>();
        ArrayList<String> pieName = new ArrayList<>();
        ArrayList<Integer> colors = new ArrayList<>();

        colors.add(Color.YELLOW);
        colors.add(Color.RED);
        colors.add(Color.BLUE);
        colors.add(Color.GREEN);


        for(int i = 0 ; i < data.length ; i++) {
            pieEntries.add(new PieEntry(data[i], i));
        }

        for(int i = 0 ; i < name.length ; i++) {
            pieName.add(name[i]);
        }

        PieDataSet pieDataSet = new PieDataSet(pieEntries, "Result");
        pieDataSet.setSliceSpace(2);
        pieDataSet.setValueTextSize(12);
        pieDataSet.setColors(colors);
        
    }

}

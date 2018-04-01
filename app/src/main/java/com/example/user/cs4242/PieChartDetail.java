package com.example.user.cs4242;

import android.app.Activity;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

/**
 * Created by User on 30/3/2018.
 */

public class PieChartDetail  extends Activity {

    TextView detail;
    TextView percetage;
    TextView detail_title;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.piechartdetail);
        detail = (TextView) findViewById(R.id.detail);
        percetage = (TextView) findViewById(R.id.percetage);
        detail_title = findViewById(R.id.detail_title);
        detail_title.setText("The " + getIntent().getStringExtra("Detail_title") + " sDetail");
        detail.setText(getIntent().getStringExtra("Detail_title"));
        percetage.setText(getIntent().getStringExtra("Percetage"));
    }
}

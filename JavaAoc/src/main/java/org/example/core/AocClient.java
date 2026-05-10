package org.example.core;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class AocClient {
    private static final HttpClient client = HttpClient.newHttpClient();
    private static final String BASE_URL = "https://adventofcode.com";

    public String fetchInput(int year, int day, String cookie) {
        try {
            String url = String.format("%s/%d/day/%d/input", BASE_URL, year, day);
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .header("Cookie", "session=" + cookie)
                    .GET()
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            if (response.statusCode() != 200) {
                throw new RuntimeException(
                        String.format("HTTP error %d fetching input for %d/day/%d", response.statusCode(), year, day)
                );
            }

            return response.body();
        } catch (Exception e) {
            throw new RuntimeException("Failed to fetch input from Advent of Code", e);
        }
    }
}


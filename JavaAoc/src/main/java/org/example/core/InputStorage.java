package org.example.core;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Optional;

public class InputStorage {
    private static final String INPUT_DIR = "inputs";

    public Optional<String> load(int year, int day) {
        try {
            Path filePath = getFilePath(year, day);
            if (Files.exists(filePath)) {
                String content = Files.readString(filePath, StandardCharsets.UTF_8);
                return Optional.of(content);
            }
            return Optional.empty();
        } catch (IOException e) {
            return Optional.empty();
        }
    }

    public void save(int year, int day, String content) {
        try {
            Path filePath = getFilePath(year, day);
            Files.createDirectories(filePath.getParent());
            Files.writeString(filePath, content, StandardCharsets.UTF_8);
        } catch (IOException e) {
            throw new RuntimeException(String.format("Failed to save input for %d/day/%d", year, day), e);
        }
    }

    private Path getFilePath(int year, int day) {
        return Paths.get(INPUT_DIR, String.valueOf(year), String.format("day%02d.txt", day));
    }
}


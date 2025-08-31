plugins {
    java
    war
}

group = "org.example"
version = "1"

repositories {
    mavenCentral()
}

dependencies {
    // Тестовые зависимости
    testImplementation(platform("org.junit:junit-bom:5.9.1"))
    testImplementation("org.junit.jupiter:junit-jupiter")

    // Jakarta EE API предоставляемые WildFly
    providedCompile("jakarta.platform:jakarta.jakartaee-web-api:9.0.0")
    providedCompile("jakarta.json:jakarta.json-api:2.1.1")
    providedCompile("jakarta.json.bind:jakarta.json.bind-api:3.0.0")
    providedCompile("jakarta.ejb:jakarta.ejb-api:4.0.1")

    // Другие зависимости
    implementation("com.google.guava:guava:31.0.1-jre")
    implementation("org.apache.commons:commons-lang3:3.12.0")
    implementation("com.google.code.gson:gson:2.8.9")
}

tasks.test {
    useJUnitPlatform()
}
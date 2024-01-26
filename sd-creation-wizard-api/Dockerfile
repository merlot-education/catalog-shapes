FROM maven:3-eclipse-temurin-17-alpine AS build

RUN apk add --no-cache git maven &&\
    git clone https://gitlab.eclipse.org/eclipse/xfsc/self-description-tooling/sd-creation-wizard-api.git &&\
    cd /sd-creation-wizard-api &&\
    git checkout ed958790fb14bd424e4148e7034195fa803d939c &&\
    mvn clean package -Dmaven.test.skip=true

FROM eclipse-temurin:17-jre-alpine
COPY --from=build /sd-creation-wizard-api/target/creation-wizard-api*.jar /opt/creation-wizard-api.jar
COPY catalog-shapes/shacl/shapes/merlot/ /shapes/

RUN rm -rf /shapes/data-types &&\
    rm /shapes/gax-service/merlot-serviceOfferingShape.ttl &&\
    mv /shapes/gax-participant /shapes/Participant &&\
    mv /shapes/gax-service /shapes/Service

ENTRYPOINT ["java", "-jar","/opt/creation-wizard-api.jar"]
